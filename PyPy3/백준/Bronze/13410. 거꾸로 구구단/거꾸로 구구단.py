N, K = map(int, input().split())
reversed_results = []

for i in range(1, K + 1): 
    result = N * i  
    reversed_result = int(str(result)[::-1])  
    reversed_results.append(reversed_result)

print(max(reversed_results))
