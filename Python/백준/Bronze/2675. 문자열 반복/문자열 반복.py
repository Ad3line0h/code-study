T = int(input())
for i in range(T):
    tokens = input().split()
    R = int(tokens[0])
    S = tokens[1]
    print(''.join(ch * R for ch in S))
