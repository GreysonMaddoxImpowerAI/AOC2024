import os

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
top_ipt = []
with open(f"{pwd}\Day5.txt", "r") as file: 
    for line in file:
        top_ipt.append([char for char in line.replace('\n', '')])

bot_ipt = []
with open(f"{pwd}\Day5-1.txt", "r") as file: 
    for line in file:
        bot_ipt.append([char for char in line.replace('\n', '')])
bot_ipt = [''.join(row).split(',') for row in bot_ipt]

mappings = dict()
for row in top_ipt:
    vals = ''.join(row).split('|')
    left, right = int(vals[0].strip()), int(vals[1].strip())
    if left not in mappings.keys():
        mappings[left] = set()
    mappings[left].add(right)
for mapping in mappings.keys():
    mappings[mapping] = list(mappings[mapping])

total, p2_total = 0, 0
for row in bot_ipt:
    row = [int(elem) for elem in row]
    row.reverse()
    tmp_mappings = dict()
    for elem in row:
        tmp_mappings[elem] = [val for val in mappings[elem] if val in row]
    sorted_tmp_mappings = {key: value for key, value in sorted(tmp_mappings.items(), key=lambda item: len(item[1]))}
    sorted_row = [key for key in sorted_tmp_mappings.keys()]
    if sorted_row == row:
        total += int(row[int(len(row) / 2)])
    else:
        p2_total += int(sorted_row[int(len(sorted_row) / 2)])
print('Part 1 Total:',total)
print('Part 2 Total:',p2_total)