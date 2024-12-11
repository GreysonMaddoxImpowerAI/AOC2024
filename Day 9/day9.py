import os
import copy

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{pwd}\Day9.txt", "r") as file: 
    for line in file:
        ipt = [int(char) for char in line.replace('\n', '')]

p1_output, p2_output = [], []
dots, nums = [], []
nums_vals = dict()
num = 0
for idx, elem in enumerate(ipt):
    if idx % 2 == 0:
        nums_vals[num] = [elem, len(p1_output)]
        for i in range(elem):
            p1_output.append(num)
        num += 1
    else:
        arr_vals = []
        for i in range(elem):
            arr_vals.append(len(p1_output))
            p1_output.append('.')
        if len(arr_vals) > 0:
            dots.append(arr_vals)
p2_output = copy.deepcopy(p1_output)
for i in range(len(p1_output)):
    try:
        if not str(p1_output[i]).isdigit():
            val = p1_output.pop()
            while not str(val).isdigit():
                val = p1_output.pop()
            p1_output[i] = val
    except:
        break
nums_vals = dict(sorted(nums_vals.items(), reverse=True))
for key in nums_vals.keys():
    for arr in dots:
        if len(arr) > 0:
            if arr[0] < nums_vals[key][1] and len(arr) >= nums_vals[key][0]:
                dots.append([j for j in range(len(p2_output)) if p2_output[j] == key])
                dots.sort()
                for i in [j for j in range(len(p2_output)) if p2_output[j] == key]:
                    p2_output[i] = '.'
                for i in range(nums_vals[key][0]):
                    p2_output[arr[i]] = key
                for i in range(nums_vals[key][0]):
                    arr.pop(0)
                break
p1_total = 0
for i in range(len(p1_output)):
    if p1_output[i] != '.':
        p1_total += (i * p1_output[i])
p2_total = 0
for i in range(len(p2_output)):
    if p2_output[i] != '.':
        p2_total += (i * p2_output[i])
print('Part 1:',p1_total)
print('Part 2:',p2_total)