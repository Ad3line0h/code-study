origin = [ 1, 1, 2, 2, 2, 8 ]

mine = list(map(int, input().split()))

for i in range(6) :
    result = origin[i] - mine[i]
    print(result)