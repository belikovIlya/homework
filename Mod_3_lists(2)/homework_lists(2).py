#task 1
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
#
# a.extend(b)
# count_five = a.count(5)
# print(f'Amount of digit <5> in first combining: {count_five}')
# for _ in range(count_five):
#     a.remove(5)
#
# a.extend(c)
# count_three = a.count(3)
# print(f'Amount of digit <3> in second combining: {count_three}')
# print(f'The final list: {a}')
#task 2
# def sort_pupil(list): #selection sort realization
#     for i_chck in range(len(list) - 1):
#         for curr in range(i_chck + 1, len(list) - 1):
#             if list[curr] < list[i_chck]:
#                 list[curr], list[i_chck] = list[i_chck], list[curr]
#     return list
#
#
# list_class_1 = list(range(160, 168, 2))
# list_class_2 = list(range(162, 173, 3))
#
# list_class_1.extend(list_class_2)
# print(f'Sorted list from pupils: {sort_pupil(list_class_1)}')
#task 3
#
# shop = [['каретка', 1200], ['шатун', 1000],
#         ['седло', 300], ['педаль', 100], ['седло', 1500],
#         ['рама', 12000], ['обод', 2000], ['шатун', 200],
#         ['седло', 2700]]
#
# det_count = 0
# det_cost = 0
# detail = input('Enter the detail name: ')
# for i_info in range(len(shop)):
#     if shop[i_info][0] == detail.lower():
#         det_count += 1
#         det_cost += shop[i_info][1]
#
# print(f'Amount of details: {det_count}')
# print(f'Total cost: {det_cost}')
#task 4
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# stop = 'пора спать'
# came = 'пришел'
# left = 'ушел'
# while True:
#     print(f'On party {len(guests)} people: {guests}')
#     print('The guest left or came? ', end='')
#     is_there = input().lower()
#     if is_there == stop:
#         break
#     guest_name = input("Enter the name of guest: ")
#     if is_there == came:
#         if len(guests) < 6:
#             print(f'Hi, {guest_name}')
#             guests.append(guest_name)
#         else:
#             print(f'Sorry, {guest_name}, there is no place for you!')
#     elif is_there == left:
#         if guest_name in guests:
#             guests.remove(guest_name)
#             print(f'Bye, {guest_name}!')
#         else:
#             print(f'Guest {guest_name} is not at the party!')
#     print()
#
# print(f'The party is over, good night!')
#task 5
# violator_songs = [
#     ['World in My Eyes', 4,54],
#     ['Sweetest Perfection', 4,43],
#     ['Personal Jesus', 4,56],
#     ['Halo', 4,42],
#     ['Waiting for the Night', 6,17],
#     ['Enjoy the Silence', 4,20],
#     ['Policy of Truth', 4,56],
#     ['Blue Dress', 4,29],
#     ['Clean', 5,33]
# ]
#
# amnt_sng = int(input("Enter the amount of songs: "))
# min_sum = 0
# sec_sum = 0
# for i_song in range(amnt_sng):
#     print(f'Name of the {i_song + 1} song: ', end=' ')
#     song_name = input()
#     for i in range(len(violator_songs)):
#         if song_name == violator_songs[i][0]:
#             min_sum += violator_songs[i][1]
#             sec_sum += violator_songs[i][2]
#             break
# if sec_sum >= 60:
#     delta = sec_sum // 60
#     delta_1 = sec_sum % 60
#     min_sum += delta
#     sec_sum = delta_1
#
# total_time = str(min_sum) + ',' + str(sec_sum)
# print(f'Total time of picked tracks: {total_time} minute')
# task 6
# lst_one = []
# lst_two = []
#
# for i in range(3):
#     query = 'Введите ' + str(i + 1) + ' число для первого списка: '
#     number = int(input(query))
#     lst_one.append(number)
#
# for i in range(7):
#     query = 'Введите ' + str(i + 1) + ' число для второго списка: '
#     number = int(input(query))
#     lst_two.append(number)
#
# print(f'The first list: {lst_one}')
# print(f'The first list: {lst_two}')
#
# lst_one.extend(lst_two)
#
# for i_elem in lst_one:
#     if lst_one.count(i_elem) > 1:
#         lst_one.remove(i_elem)
#
# print(lst_one)
#task 7
# roll_sizeL = []
# leg_sizeL = []
# count = 0
# amnt_ski = int(input("Enter the amount of roller skates: "))
# for i_el in range(amnt_ski):
#     print(f'Size of {i_el + 1} pair is: ')
#     roll_size = input()
#     roll_sizeL.append(roll_size)
#
# amnt_ppl = int(input("Enter the amount of people: "))
# for i_el in range(amnt_ppl):
#     print(f'Size of leg the {i_el + 1} man: ')
#     leg_size = input()
#     leg_sizeL.append(leg_size)
#
# for leg in leg_sizeL:
#     for roll in roll_sizeL:
#         if leg <= roll:
#             roll_sizeL.remove(roll)
#             count += 1
# print(f'The biggest amount people, who can take roller skates: {count}')
#task 8
# people = int(input('Amount of people: '))
# dropped = int(input('What is the number in the game? '))
# print('Dropped out every', dropped, 'man.')
# people_list = list(range(1, people + 1))
# out = 0
# for _ in range(len(people_list) - 1):
#     print('\nCurrent list of people: ', people_list)
#     start_count = out % len(people_list)
#     out = (start_count + dropped - 1) % len(people_list)
#     print('The beginning ', people_list[start_count])
#     print('Dropped man who have number ', people_list[out])
#     people_list.remove(people_list[out])
#
# print('Last: ', *people_list)
#task 9
# friend = int(input('Кол-во друзей: '))
# receipt = int(input('Долговых расписок: '))
# friends_list = []
#
# for _ in range(friend):
#     friends_list.append(0)
#
# for el in range(receipt):
#     print(f'{el + 1} receipt')
#     to = int(input("Enter to: "))
#     from_who = int(input('From: '))
#     amnt = int(input('How much: '))
#     friends_list[from_who - 1] += amnt
#     friends_list[to - 1] -= amnt
#
# print('\nBalance of friends:')
# for index in range(len(friends_list)):
#     print(f'{index + 1} : {friends_list[index]}')
#task 10
# def is_palindrom(num_list):
#     reverse_list = []
#     for i_num in range(len(num_list) - 1, -1, -1):
#         reverse_list.append(num_list[i_num])
#     if num_list == reverse_list:
#         return True
#     else:
#         return False
#
# nums = [1, 2, 3, 4, 5]
# new_nums = []
# answer = []
#
# for i_nums in range(0, len(nums)):
#     for j_elem in range(i_nums, len(nums)):
#         new_nums.append((nums[j_elem]))
#     if is_palindrom(new_nums):
#         for i_answer in range(0, i_nums):
#             answer.append(nums[i_answer])
#         answer.reverse()
#         break
#     new_nums = []
#
# print(f'List #1 : {nums}')
# print(f'Need nums: {len(answer)}')
# print(f'List #2: {answer}')

