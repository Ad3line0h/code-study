T = int(input())
for i in range(T):                
    tokens = input().split()
    value = float(tokens[0])       

    for op in tokens[1:]:         
        if op == '@':
            value *= 3
        elif op == '%':
            value += 5
        elif op == '#':
            value -= 7

    print(f"{value:.2f}")         
