A, B, C = map(int, input().split())
D = int(input())

total_seconds = A * 3600 + B * 60 + C
total_seconds += D

hour = total_seconds // 3600 % 24
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(hour, minute, second)
