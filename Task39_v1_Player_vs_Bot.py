# Задача 39 против обычного бота.

import random

with open('Task39_total_candies.txt', 'w') as total_candies:
    total_candies.write(input('Введите стартовое количество конфет: '))

with open('Task39_total_candies.txt', 'r') as total_candies:
    total_candies = int(total_candies.read())
    
candies_bottom_limit = 1
candies_top_limit = 28
print(f'Конфет на столе: {total_candies}')
temp_candies = total_candies
while temp_candies > 0:
    player1_move = int(input(f'Заберите от 1 до 28 конфет: '))
    if candies_bottom_limit <= player1_move < candies_top_limit+1:
        temp_candies -= player1_move
    else:
        print('Неверный ход!', end = '')
        break
    if temp_candies <= 0:
        temp_candies = 0
        print(f'Конфет на столе: {temp_candies}.\nВы победили бота.')
        break
    print(f'Конфет на столе: {temp_candies}.')

    

    if temp_candies > 0:
        bot_move = int(random.randint(1,29))
        print(f'Бот забирает от 1 до 28 конфет: {bot_move}')
        if 0 < bot_move < 29:
            temp_candies -= bot_move
        else:
            print('Неверный ход!', end = '')
        if temp_candies <= 0:
            temp_candies = 0
            print(f'Конфет на столе: {temp_candies}.\nБот Вас победил.')
            break
    print(f'Конфет на столе: {temp_candies}.')
print(' КОНЕЦ ИГРЫ')