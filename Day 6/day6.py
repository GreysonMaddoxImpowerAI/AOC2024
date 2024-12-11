import os
import time
import copy

def MakeGuardMove(arr, dir, cur_loc):
    new_dir = dir
    while arr[cur_loc[0] + new_dir[0]][cur_loc[1] + new_dir[1]] == '#':
        if new_dir == (-1, 0):
            new_dir = (0, 1)
        elif new_dir == (0, 1):
            new_dir = (1, 0)
        elif new_dir == (1, 0):
            new_dir = (0, -1)
        else:
            new_dir = (-1, 0)
    return [(cur_loc[0] + new_dir[0], cur_loc[1] + new_dir[1]), new_dir]

    
pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
ipt = []
with open(f"{pwd}\Day6.txt", "r") as file: 
    for line in file:
        ipt.append([char for char in line.replace('\n', '')])

for row in ipt:
    print(''.join(row))

print()

p2_locs = []
for row_num, row in enumerate(ipt):
    for col_num, col in enumerate(row):
        if ipt[row_num][col_num] == '^':
            guard_loc = (row_num, col_num)
        elif ipt[row_num][col_num] == '.':
            p2_locs.append((row_num, col_num))
dir = (-1, 0)

ipt[guard_loc[0]][guard_loc[1]] = '.'

traveled_locs = dict()
cycles = []
for loc in p2_locs:
    tmp_traveled_locs = copy.deepcopy(traveled_locs)
    tmp_ipt = copy.deepcopy(ipt)
    tmp_guard_loc = copy.deepcopy(guard_loc)
    dir = (-1,0)
    tmp_ipt[loc[0]][loc[1]] = '#'
    cycle = False
    while True:
        if tmp_guard_loc not in tmp_traveled_locs.keys():
            tmp_traveled_locs[tmp_guard_loc] = [dir]
        elif dir in tmp_traveled_locs[tmp_guard_loc]:
            cycle = True
            break
        else:
            tmp_traveled_locs[tmp_guard_loc].append(dir)
        tmp_ipt[tmp_guard_loc[0]][tmp_guard_loc[1]] = 'X'
        if tmp_guard_loc[0] + dir[0] < 0 or tmp_guard_loc[1] + dir[1] < 0:
            break
        try:
            tmp_guard_loc, dir = MakeGuardMove(tmp_ipt,dir,tmp_guard_loc)
        except:
            break
    print(loc, cycle)
    if cycle:
        cycles.append(loc)

total_spaces = 0
print(len(cycles))