numbers = list(map(int, input().split()))
squares_sum = sum(n**2 for n in numbers)
checksum = squares_sum % 10
print(checksum)