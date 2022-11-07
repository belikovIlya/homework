def sum_num(numb):
    sum = 0
    while numb != 0:
        last_num = numb % 10
        sum += last_num
        numb //= 10
    return sum

print(sum_num(inp_numb) - amount_num(inp_num))