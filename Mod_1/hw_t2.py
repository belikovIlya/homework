def reverse_1(inpt_number):
    whole = ''
    fraction = ''
    flag = True
    for sym in inpt_number:
        if sym == '.':
            flag = False
        elif flag == True:
            fraction += sym
        else:
            whole += sym
    return float(fraction[::-1] + '.' + whole[::-1])


K = input("Enter the K number: ")
N = input("Enter the N number: ")
res_K = reverse_1(K)
res_N = reverse_1(N)
print(res_K, res_N)
total_sum = round(float(res_K + res_N), 3)
print(total_sum)
