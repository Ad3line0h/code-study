L, R, A = map(int, input().split())
k = min(L + A, R + A, (L + R + A) // 2)
print(k * 2)