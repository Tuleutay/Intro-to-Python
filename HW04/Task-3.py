# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

nums = list(map(int, input("Введите числа через пробел: ").split(" ")))
def list_of_non_repeating_elements(list):
    i=0
    while i < len(list):
        x = list[i]
        if list.count(x)>1:
            while list.count(x)>0:
                list.remove(x)
        else:
            i+=1
    return list
result = list_of_non_repeating_elements(nums)
print(result)