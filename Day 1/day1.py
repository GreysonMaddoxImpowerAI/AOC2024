import os

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
print(pwd)
ipt = ""
with open(f"{pwd}\Day1.txt", "r") as file: 
    for line in file:
        ipt += line
left, right = [], []
for line in ipt.splitlines():
    left.append(int(line.split('  ')[0]))
    right.append(int(line.split('  ')[1]))
left.sort()
right.sort()
diffs = [abs(right[i] - left[i]) for i in range(len(right))]
print(f'Part 1: {sum(diffs)}')
ids = dict()
total = 0
for i in left:
    if i not in ids.keys():
        matches = len([j for j in range(len(right)) if right[j] == i])
        ids[i] = matches
    total += i * ids[i]
print(f'Part 1: {total}')
