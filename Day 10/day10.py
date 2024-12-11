import os
import copy

def CheckDirections(elem, val, ipt):
    output = []
    if elem[0] - 1 >= 0:
        if ipt[elem[0] - 1][elem[1]] == val + 1:
            output.append([(elem[0] - 1, elem[1]), val + 1])
    if elem[0] + 1 < len(ipt):
        if ipt[elem[0] + 1][elem[1]] == val + 1:
            output.append([(elem[0] + 1, elem[1]), val + 1])
    if elem[1] - 1 >= 0:
        if ipt[elem[0]][elem[1] - 1] == val + 1:
            output.append([(elem[0], elem[1] - 1), val + 1])
    if elem[1] + 1 < len(ipt[0]):
        if ipt[elem[0]][elem[1] + 1] == val + 1:
            output.append([(elem[0], elem[1] + 1), val + 1])
    return output

ipt = []
pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{pwd}\Day10.txt", "r") as file: 
    for line in file:
        ipt.append([int(char.replace('.', '-1')) for char in line.replace('\n', '')])

elems = []
for row_idx, row in enumerate(ipt):
    for col_idx, col in enumerate(row):
        if col == 0:
            elems.append([(row_idx, col_idx), 0])
p1_total, p2_total = 0, 0
for zero in elems:
    print(f'CHECKING {zero[0]}')
    paths = [zero]
    nines_found = set()
    while len(paths) > 0:
        val = paths.pop(0)
        dirs =  CheckDirections(val[0], val[1], ipt)
        for dir in dirs:
            if dir[1] != 9:
                paths.insert(0, dir)
            else:
                nines_found.add(dir[0])
                p2_total += 1
    p1_total += len(nines_found)
print(p1_total)
print(p2_total)