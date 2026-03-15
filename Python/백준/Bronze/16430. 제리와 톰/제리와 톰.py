A, B = map(int, input().split())
P = B - A
Q = B

a, b = P, Q
while b != 0:
    a, b = b, a % b
gcd = a

print(P // gcd, Q // gcd)