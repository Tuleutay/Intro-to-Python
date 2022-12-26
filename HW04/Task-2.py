# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n=int(input('Введите натуральное число '))
# num=[]
# for i in range(1,10):
#     if i//n==0:
#         num.append(i)
# print(num)

a = int(input('Задайте натуральное число '))
def check_nat_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_table_num(num):
    table_natural_number = []
    for i in range(2, num + 1):
        if check_nat_num(i):
            table_natural_number.append(i, )
    table_natural_number.insert(0, 1)
    return table_natural_number



listOfNaturalsNumbers = get_table_num(a)
print(listOfNaturalsNumbers)


def get_degree_of_number(num):
    list_of_number_and_degree = []
    i = 1
    degree = 0
    for i in listOfNaturalsNumbers:
        while num > 1:
            if num / listOfNaturalsNumbers[i] - int(num / listOfNaturalsNumbers[i]) != 0:
                i += 1
            while num > 1 and num / listOfNaturalsNumbers[i] - int(num / listOfNaturalsNumbers[i]) == 0:
                num = num / listOfNaturalsNumbers[i]
                degree += 1
            list_of_number_and_degree.extend([listOfNaturalsNumbers[i], degree])
            #print(list_of_number_and_degree)
            degree = 0
            break
    return list_of_number_and_degree


result = get_degree_of_number(a)
print(result)


