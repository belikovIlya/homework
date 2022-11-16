#task 1
# new_list = []
# N = int(input("Enter the end of list: "))
# for i in range(1, N + 1, 2):
#     new_list.append(i)
# print(new_list)
#task 2
# name_list = ['Артемий', 'Борис',
#              'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# first_day = []
# for index, name in enumerate(name_list):
#     if index % 2 == 0:
#         first_day.append(name)
# print(f'1st day: {first_day}')
#task 3
# list_cell = []
# amnt_cell = int(input("Enter the amount of cell: "))
# for i in range(amnt_cell):
#     eff = int(input(f"Enter the effect for {i + 1} cell: "))
#     list_cell.append(eff)
# #list_cell = [3, 0, 6, 2, 10]
# cell_below = []
# for i in range(0, len(list_cell)):
#     print(f'Effect {i + 1} cell is: {list_cell[i]}')
#     if i > list_cell[i]:
#         cell_below.append(list_cell[i])
# print(cell_below)
#task 4
# def delete_newest(list_rtx):
#     new_rtx = []
#     max_model = list_rtx[0]
#     for i in list_rtx:
#         if i > max_model:
#             max_model = i
#     for i in list_rtx:
#         if i != max_model:
#             new_rtx.append(i)
#     return new_rtx
#
# list_rtx = []
# amnt_rtx = int(input("Enter the amount of RTX: "))
# for i in range(amnt_rtx):
#      model = int(input(f"Enter the model for {i + 1} RTX: "))
#      list_rtx.append(model)
# print(list_rtx)
#
# print(f'New list of RTX: {delete_newest(list_rtx)}')
#task 5
# def favourite_films(amount, films_list):
#     lovely_films = []
#     for _ in range(amount):
#         name_film = input("Enter the film name: ")
#         for film in films_list:
#             if name_film in films_list:
#                 lovely_films.append(name_film)
#                 break
#             else:
#                 print(f'We have not the {name_film}')
#                 break
#     return lovely_films
#
# def list_to_str(list):
#     fav_mov = ''
#     for c in range(len(list)):
#         fav_mov += list[c]
#         if c < len(list) - 1:
#             fav_mov += ', '
#     return fav_mov
#
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
# 'Богемская рапсодия', 'Город грехов', 'Мементо',
# 'Отступники', 'Деревня']
# size = int(input('Enter the amount of checked films: '))
# list_1 = favourite_films(size, films)
# print(f'Your list of lovely films: {list_to_str(list_1)}')
#task 6
# word_1 = 'privet'
# word_2 = 'lava'
# #list_word_1 = list(word_1) # ['p','r','i','v','e','t']
# #list_word_2 = list(word_2) # ['l','a','v','a']
# unique = 0
# for letter in word_2:
#     count = 0
#     for i in word_2:
#         if letter == i:
#             count += 1
#     if count == 1:
#         unique += 1
# print(f'Amount of unique letter: {unique}')
#task 7
# amnt = int(input('Enter the amount of containers: '))
# cont_list = []
# row = 0
# for i in range(amnt):
#     while True:
#         query_string = 'Enter the weight ' + str(i + 1) + ' container '
#         weight = int(input(query_string))
#         if 0 < weight <= 200:
#             break
#     cont_list.append(weight)
# new_weight = int(input('Enter the weight of NEW container: '))
# for c in range(len(cont_list)):
#     row = c + 1
#     if cont_list[c] < new_weight:
#         break
# print("Number of place for NEW container: ", row)
#task 8
# task = [] #[1, 4, -3, 0, 10]
# number = int(input('Сколько будет задач: '))
# for i in range(number):
#     task_id = int(input('Введите номер задачи: '))
#     task.append(task_id)
# print('Изначальный список:', task)
# shift = int(input('Сдвиг: '))
# task_1 = task[-shift:]
# task_2 = task[:-shift]
# task = task_1 + task_2
# print('Сдвинутый список:', task)
#task 9
# def rec_palindrom(word):
#     if len(word) < 1:
#         return True
#     else:
#         if word[0] == word[-1]:
#             return rec_palindrom(word[1:-1])
#         else:
#             return False
# str = input("Enter the word: ")
# if (rec_palindrom(str) == True):
#     print('It`s OK!')
# else:
#     print('It`s not OK! :(')
#task 10 Быстрая сортировка
# def quick_sort(list):
#     less = []
#     greater = []
#     equal = []
#     if len(list) <= 1:
#         return list
#
#     else:
#         pivot = list[0]
#         for elem in list:
#             if elem < pivot:
#                 less.append(elem)
#             elif elem > pivot:
#                 greater.append(elem)
#             elif elem == pivot:
#                 equal.append(elem)
#         return quick_sort(less) + equal + quick_sort(greater)
#
# print(quick_sort([7,6,10,5,9,8,7,3,4]))
#
#
