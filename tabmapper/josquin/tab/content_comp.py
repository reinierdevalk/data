import os
import sys

args = sys.argv

file1 = args[1]
file2 = args[2]

with open(file1) as f:
	lines1 = f.readlines()

with open(file2) as f:
	lines2 = f.readlines()

if len(lines1) != len(lines2):
	print(f"length of file1 ({len(lines1)}) is not the same as length of file2 ({len(lines2)})")

diff_found = False
for i in range(0, len(lines1)):
	if not lines1[i] == lines2[i]:
		print(f"line {i} is different:\n{lines1[i]}vs\n{lines2[i]}")
		diff_found = True
if diff_found == False:
	print("files are the same")

