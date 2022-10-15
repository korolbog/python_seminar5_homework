# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B4%D0%BB%D0%B8%D0%BD_%D1%81%D0%B5%D1%80%D0%B8%D0%B9#:%7E:text=run%2Dlength%20encoding%2C%20RLE),%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%89%D0%B0%D1%8F%20%D0%B8%D0%B7%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D0%BE%D0%B4%D0%B8%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2%D1%8B%D1%85%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2

with open('Task42_encoder_input_data.txt', 'w') as message:
    message.write(input('Введите сообщение для сжания: '))

with open('Task42_encoder_input_data.txt', 'r') as message:
    message = message.read()
    print(f'Сообщение для сжатия: {message}')
    compressed_message = ''
    i = 0
    while i < len(message):
        count = 1
        j = i
        while j < len(message)-1:
            if message[j] == message[j + 1]:
                count += 1
                j += 1
            else:
                break
        compressed_message = compressed_message + str(count) + message[i]
        i = j + 1
    print(f'Сжатое сообщение: {compressed_message}')
with open('Task42_encoder_output_data.txt', 'w') as data:
    data.write(compressed_message)