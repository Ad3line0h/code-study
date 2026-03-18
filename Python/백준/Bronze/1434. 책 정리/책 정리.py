N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

waste = 0
box_idx = 0
remaining = A[0]

for j in range(M):
    if B[j] <= remaining:
        remaining -= B[j]
    else:
        waste += remaining
        box_idx += 1
        remaining = A[box_idx] - B[j]

waste += remaining  

for k in range(box_idx + 1, N):
    waste += A[k]

print(waste)