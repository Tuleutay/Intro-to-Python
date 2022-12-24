# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Пример:
#  - 6782 -> 23
# - 0,56 -> 11

# num = input("Введите дробное: ")
#
# x = num.split(".")
# a = int(x[0])
# b = int(x[1])
# sum = 1
# while (a != 0):
#     sum = sum + (a % 10)
#     a = a // 10
# while (b != 0):
#     sum = sum + (b % 10)
#     b = b // 10
# print("Произведение цифр равно:", sum)

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

s = '-0.56'
summ = 0
for i in s:
    if i.isdigit():
        summ += int(i)
print(summ)


