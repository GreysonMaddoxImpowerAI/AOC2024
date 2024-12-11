import os

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
ipt = ""
with open(f"{pwd}\Day2.txt", "r") as file: 
    for line in file:
        ipt += line
og_safe, new_safe = 0, 0

def checkSafety(line, pop_idx=False, popped_idx=0):
    nums = [int(i) for i in line.split(' ')]
    if pop_idx == True:
        nums.pop(popped_idx)
    if nums[1] - nums[0] < 0:
        dir = -1
    elif nums[1] - nums[0] > 0:
        dir = 1
    else:
        return [False, 0]
    for i in range(len(nums) - 1):
        if abs(nums[i + 1] - nums[i]) not in [1, 2, 3]:
            return [False, i]
        if nums[i + 1] - nums[i] < 0:
            cur_dir = -1
        elif nums[i + 1] - nums[i] > 0:
            cur_dir = 1
        if cur_dir != dir:
            return [False, i]
    return [True, 0]
    
for line in ipt.splitlines():
    line_safe = checkSafety(line)
    if line_safe[0]:
        og_safe += 1
    else:
        for i in range(len(line.split(' '))):
            line_safe = checkSafety(line,True,i)
            if line_safe[0]:
                new_safe += 1
                break

print(f'Part 1: {og_safe}')
print(f'Part 2: {og_safe + new_safe}')