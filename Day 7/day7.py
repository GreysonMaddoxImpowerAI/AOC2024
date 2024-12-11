import os
import time
import copy

    
pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
ipt = []
with open(f"{pwd}\Day7.txt", "r") as file: 
    for line in file:
        ipt.append([char for char in line.replace('\n', '')])

total = 0
for row in ipt:
    row_total = int(''.join(row).split(':')[0])
    check_vals = [int(val) for val in ''.join(row).split(":")[1].strip().split(' ')]
    next_options = [(0,check_vals[0])]
    for idx, val in enumerate(check_vals[1:]):
        prev_options = copy.deepcopy(next_options)
        next_options = []
        for option in prev_options:
            next_options.append((option[0] + 1, option[1] + val))
            next_options.append((option[0] + 1, option[1] * val))
            next_options.append((option[0] + 1, int(str(option[1]) + str(val))))
    if len([option for option in next_options if option[1] == row_total]) > 0:
        total += row_total
print(total)