import os
import re
import numpy as np

def find_matches(row):
    cur_matches = 0
    reverse_row = ''.join(row)[::-1]
    cur_matches += len(re.findall('XMAS', ''.join(row)))
    cur_matches += len(re.findall('XMAS', ''.join(reverse_row)))
    return cur_matches

pwd = dir_path = os.path.dirname(os.path.realpath(__file__))
ipt = []
with open(f"{pwd}\Day4.txt", "r") as file: 
    for line in file:
        ipt.append([char for char in line.replace('\n', '')])
matches = 0
ipt = np.array(ipt)
for row in ipt:
    matches += find_matches(row)
transposed_ipt = np.transpose(ipt)
for row in transposed_ipt:
    matches += find_matches(row)
num_ipt = np.matrix(ipt)
for i in range(-len(ipt[0]) + 1,len(ipt)):
    matches += find_matches(np.diagonal(num_ipt, i))
transposed_num_ipt = np.fliplr(num_ipt)
for i in range(-len(ipt[0]) + 1,len(ipt)):
    matches += find_matches(np.diagonal(transposed_num_ipt, i))
print('Part 1 Answer: ' + str(matches))
p2_matches = 0
indices = []
for i in range(len(ipt)):
    for j in range(len(ipt)):
        if ipt[i:i+3,j:j+3].shape == (3,3):
            tmp_ipt = ipt[i:i+3,j:j+3].copy()
            tmp_transposed_ipt = np.fliplr(tmp_ipt.copy())
            if ('MAS' in ''.join(tmp_ipt.diagonal()) or 'SAM' in ''.join(tmp_ipt.diagonal())) and ('MAS' in ''.join(tmp_transposed_ipt.diagonal()) or 'SAM' in ''.join(tmp_transposed_ipt.diagonal())):
                p2_matches += 1
                indices.append((i, j + 2))
print('Part 2 Answer: ' + str(p2_matches))