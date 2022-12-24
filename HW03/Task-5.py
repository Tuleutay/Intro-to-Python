# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
def fib(n):
    if n==0:
        return 0
    elif n in [1, 2]:
        return 1
    elif n>2:
        return fib(n - 1) + fib(n - 2)
    else:
        return -fib(n*(-1))



a = int(input('ведите число '))
list = []
for e in range((-a), a+1):
    list.append((fib(e)))
print(list)
