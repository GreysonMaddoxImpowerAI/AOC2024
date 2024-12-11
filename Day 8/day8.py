import os
from itertools import combinations

def CalculateDifference(val1, val2):
    return (val2[0] - val1[0], val2[1] - val1[1])

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
ipt = []
with open(f"{pwd}\Day8.txt", "r") as file: 
    for line in file:
        ipt.append([char for char in line.replace('\n', '')])

vals = dict()

for row_idx, row in enumerate(ipt):
    for col_idx, val in enumerate(row):
        if val != '.':
            if val not in vals.keys():
                vals[val] = []
            vals[val].append((row_idx, col_idx))
p2_new_outputs = []
combos = []
for val_key in vals.keys():
    tmp_combos = [c for c in combinations(vals[val_key], 2)]
    total = 0
    for val in vals[val_key]:
        for c in tmp_combos:
            if c[0] == val or c[1] == val:
                total += 1
        if total > 1:
            p2_new_outputs.append(val)
    for combo in combinations(vals[val_key], 2):
        combos.append(combo)    

outputs = []
for combo in combos:
    val1 = combo[0]
    val2 = combo[1]
    if val2[1] < val1[1]:
        tmp_val = val1
        val1 = val2
        val2 = tmp_val
    diff = CalculateDifference(val1, val2)
    newval1 = (val1[0] - diff[0], val1[1] - diff[1])
    newval2 = (val2[0] + diff[0], val2[1] + diff[1])
    if newval1[0] >= 0 and newval1[0] < len(ipt) and newval1[1] >= 0 and newval1[1] < len(ipt[0]):
        outputs.append(newval1)
        newval1 = (newval1[0] - diff[0], newval1[1] - diff[1])
    while newval1[0] >= 0 and newval1[0] < len(ipt) and newval1[1] >= 0 and newval1[1] < len(ipt[0]):
        p2_new_outputs.append(newval1)
        newval1 = (newval1[0] - diff[0], newval1[1] - diff[1])
    if newval2[0] >= 0 and newval2[0] < len(ipt) and newval2[1] >= 0 and newval2[1] < len(ipt[0]):
        outputs.append(newval2)
        newval2 = (newval2[0] + diff[0], newval2[1] + diff[1])
    while newval2[0] >= 0 and newval2[0] < len(ipt) and newval2[1] >= 0 and newval2[1] < len(ipt[0]):
        p2_new_outputs.append(newval2)
        newval2 = (newval2[0] + diff[0], newval2[1] + diff[1])
print('Part 1:', len(set(outputs)))
print('Part 2:',len(set(outputs + p2_new_outputs)))