# words_list = []
# counts = [0, 0, 0]
#
# for i in range(3):
#     print(f'Enter the {i + 1} word: ')
#     word = input()
#     words_list.append(word)
#
# text = input('Enter the word from text: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input('Enter the word from text: ')
#
# print('\nCount words in text: ')
# for i in range(3):
#     print(words_list[i], ':', counts[i])
#--------------------------------------------------------
# input_str = input("Enter the string: ")
# letters = list(input_str)
# what = ':'
# for_what = ';'
# count = 0
# for letter in letters:
#     print(letter, end='')
# print()
#
# for index, value in enumerate(letters):
#     if value == what:
#         letters[index] = for_what
#         count += 1
#
# for letter in letters:
#     print(letter, end='')
# print(f'\nAmount of exchanges: {count}')
#----------------------------------------------------------
# word_str = input("Enter the string: ")
# list_words = list(word_str)
# index_sym = int(input("Enter the index symbol")) - 1
# count = 0
# if index_sym > 0:
#     print(f'Left element is: {list_words[index_sym - 1]}')
#     if list_words[index_sym - 1] == list_words[index_sym]:
#         count += 1
# if index_sym < len(list_words):
#     print(f'Right element is: {list_words[index_sym + 1]}')
#     if list_words[index_sym + 1] == list_words[index_sym]:
#         count += 1
# if count == 0:
#     print("Таких же символов нет.")
# elif count == 1:
#     print("Есть ровно один такой же символ.")
# elif count == 2:
#     print("Таких символов два.")