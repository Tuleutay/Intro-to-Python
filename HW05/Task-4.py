# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# def compression(sequence):
#     count = 1
#     result = []
#     for x, item in enumerate(sequence):
#         if x == 0:
#             continue
#         elif item == sequence[x - 1]:
#             count += 1
#         else:
#             result.append((sequence[x - 1], count))
#             count = 1
#     result.append((sequence[len(sequence) - 1], count))
#     return result
#
#
# def decode(sequence):
#     result = []
#     for item in sequence:
#         result.append(item[0] * item[1])
#
#     return "".join(result)
#
#
# def formatOutput(sequence):
#     result = []
#     for item in sequence:
#         if (item[1] == 1):
#             result.append(item[0])
#         else:
#             result.append(str(item[1]) + item[0])
#
#     return "".join(result)
#
#
# s = input("input sequence ")
#
# compressed = compression(s)
# decoded = decode(compressed)
#
# print("Compressed Result: " + formatOutput(compressed))
# print("Decoded Result: " + decoded)
with open('text.txt','r') as file:
    file = file.read
with open('RLE.txt', 'w') as rle:
    while   len(file)>1:
        i=1
        while file[0]==file[1]:
            i+=1
        rle.write(f'{file[0]} {i}\n')
        file = file[i:]


