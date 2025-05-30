N = int(input())

# 윗부분
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# 아랫부분
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
