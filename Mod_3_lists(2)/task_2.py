# pack = []
# decode = []
# bad_packs = 0
# packs_amnt = int(input("Enter the amount of packs: "))
#
# for i_pack_num in range(packs_amnt):
#     print(f'\nPack num: {i_pack_num + 1} ')
#     for i_bit in range(4):
#         print(i_bit + 1, 'bit', end=' ')
#         num = int(input())
#         pack.append(num)
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Too much errors!')
#         bad_packs += 1
#     pack = []
#
# print(f'\nMessage for decode: {decode}')
# print(f'Amount of error in message: {decode.count(-1)}')
# print(f'Amount of loss packs: {bad_packs}')
#---------------------------------------------------------
# first_msg = input('The first message: ')
# scnd_msg = input('The second message: ')
#
# first_count = first_msg.count('?') + first_msg.count('!')
# scnd_count = scnd_msg.count('?') + scnd_msg.count('!')
#
# if first_count < scnd_count:
#     first_msg, scnd_msg = scnd_msg, first_msg
#     third_msg = first_msg + scnd_msg
#     print(f'The third message: {third_msg}')
# else:
#     print(f'Third message: {first_msg + scnd_msg}')
#----------------------------------------------------------
packet = []
message = []
bad_packet = 0
amnt_packet = int(input('Enter the amount of packets: '))

for i_elem in range(amnt_packet):
    print(f'Packet number {i_elem + 1}: ')
    for i_bit in range(4):
        print(f'{i_bit + 1} bit: ', end=' ')
        bit = int(input())
        packet.append(bit)
    if packet.count(-1) <= 1:
        message.extend(packet)
    else:
        print(f'In packet ---{packet}--- too much error!')
        bad_packet += 1
    packet = []
print(f'Message: {message}')
print(f'Amount of error in message: {message.count(-1)}')
print(f'Amount of loss packet: {bad_packet}')