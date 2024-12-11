import os
import re

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
ipt = ""
with open(f"{pwd}\Day3.txt", "r") as file: 
    for line in file:
        ipt += line
vals = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", ipt)
vals = [str(val) for val in vals]
print(vals)
vals = [val.replace('mul','').replace('(', '').replace(')','') for val in vals]
print(vals)
activated = True
total = 0
for val in vals:
    if activated and 'do' not in val:
        print(f'Multiplying {val}')
        total += int(val.split(',')[0]) * int(val.split(',')[1])
        continue
    if 'don' in val:
        activated = False
    elif 'do' in val:
        activated = True
print(total)
# print(sum([int(val.split(',')[0]) * int(val.split(',')[1]) for val in vals]))