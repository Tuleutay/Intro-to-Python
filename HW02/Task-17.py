# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] -
#  списко на основе n, а позиции элементов lst2=[3,1].
n=int(input('введите число '))
lst2=[3,1]
lst1=[]
mult = 1
for i in range(1,n+1):
    from random import randint
    element = randint(-n,n)
    lst1.append(element)
print(lst1)
for e in range(len(lst2)):
    a = lst2[e]
    mult = mult * lst1[a]
print(mult)