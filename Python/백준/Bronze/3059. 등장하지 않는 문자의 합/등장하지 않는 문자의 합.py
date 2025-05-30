import sys

lines = sys.stdin.read().splitlines()
T = int(lines[0])

ASCII_A_TO_Z_SUM = sum(range(ord('A'), ord('Z') + 1))

for i in range(1, T + 1):
    S = lines[i]
    unique_chars = set(S)
    sum_used = sum(ord(c) for c in unique_chars)
    print(ASCII_A_TO_Z_SUM - sum_used)

