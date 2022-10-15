# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B4%D0%BB%D0%B8%D0%BD_%D1%81%D0%B5%D1%80%D0%B8%D0%B9#:%7E:text=run%2Dlength%20encoding%2C%20RLE),%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%89%D0%B0%D1%8F%20%D0%B8%D0%B7%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D0%BE%D0%B4%D0%B8%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2%D1%8B%D1%85%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2

import re

with open('Task42_encoder_output_data.txt', 'r') as compressed_message:
    compressed_message = compressed_message.read()
print(f'Сжатое сообщение: {compressed_message}')
decompressed_message = ''

counts = list(map(int, (re.findall(r'\d+',compressed_message))))
letters = list(re.findall(r'[a-zA-Z]+',compressed_message))

for i in range(len(counts)):
    for j in range(counts[i]):
        decompressed_message = decompressed_message + letters[i]
print(f'Распакованное сообщение:\n{decompressed_message}')