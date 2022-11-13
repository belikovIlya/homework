nums_list = []
N = int(input('Кол-во чисел в списке: '))
for i in range(N):
    num = int(input(f' Enter the {i+1} число: '))
    nums_list.append(num)
print()
K = int(input("Enter the divider: "))
index = 0
sum_index = 0

for i in nums_list:
    if i % K == 0:
        print(f'Index num {i} is: {index}')
        sum_index += index
    index += 1

print(f'Sum of indexes: {sum_index}')