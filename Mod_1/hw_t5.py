def min_div(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
        else:
            continue
    return 0

inp_n = int(input("Enter the number which > 1: "))
print(f'Minimal divider {inp_n} is {min_div(inp_n)}')