# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
from typing import List, Any

n=int(input('введите число '))
x=[]
sum = 0
for i in range(1,n+1):
    element = (1+1/i)**i
    x.append(element)
    sum = sum + element
print(x)
print(sum)
