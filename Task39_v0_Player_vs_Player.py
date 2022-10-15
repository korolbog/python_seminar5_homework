# Создайте программу для игры с конфетами человек против человека.
# # Условие задачи:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, # чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

with open('Task39_total_candies.txt', 'w') as total_candies:
    total_candies.write(input('Введите стартовое количество конфет: '))

with open('Task39_total_candies.txt', 'r') as total_candies:
    total_candies = int(total_candies.read())

print(f'Конфет на столе: {total_candies}')
temp_candies = total_candies
while 0 < temp_candies:
    player1_move = int(input(f'Игрок 1 забирает конфет (от 1 до 28): '))
    if 0 < player1_move < 29:
        temp_candies -= player1_move
    else:
        print('Неверный ход!', end = '')
        break
        if temp_candies < 0:
            temp_candies = 0
    print(temp_candies)

    player2_move = int(input(f'Игрок 2 забирает конфет (от 1 до 28): '))
    if 0 < player2_move < 29:
        temp_candies -= player2_move
    else:
        print('Неверный ход!', end = '')
        break
        if temp_candies < 0:
            temp_candies = 0
    print(temp_candies)
print(' КОНЕЦ ИГРЫ')