# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
# for i in range(N):
#     num = int(input(f' Enter the {i+1} число: '))
#     nums_list.append(num)
# print()
# K = int(input("Enter the divider: "))
# index = 0
# sum_index = 0
#
# for i in nums_list:
#     if i % K == 0:
#         print(f'Index num {i} is: {index}')
#         sum_index += index
#     index += 1
#
# print(f'Sum of indexes: {sum_index}')

dog_list = [3, 22, 11, 5, 114, 93]
min_num = dog_list[0]
max_num = dog_list[0]
min_index = 0
max_index = 0
for index, i in enumerate(dog_list):
    if max_num < i:
        max_num = i
        max_index = index
    if min_num > i:
        min_num = i
        min_index = index
print(f'Max_num is {max_num}, max_index is {max_index}')
print(f'Min_num is {min_num}, min_index is {min_index}')
print(f'Dog list is: {dog_list}')
dog_list[min_index], dog_list[max_index] = dog_list[max_index], dog_list[min_index]
print(f'Reversed min_max Dog list is: {dog_list}')