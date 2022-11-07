def sum_num(numb):
    sum = 0
    while numb != 0:
        last_num = numb % 10
        sum += last_num
        numb //= 10
    return sum

def amount_num(numb):
    amnt = 0
    while numb != 0:
        numb //= 10
        amnt += 1
    return amnt

inp_numb = int(input("Enter the number: "))
print(sum_num(inp_numb) - amount_num(inp_numb))