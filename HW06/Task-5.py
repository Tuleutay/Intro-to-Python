# Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел,
# записанных через пробел. Необходимо выделить значения, присутствующие в обоих списках и оставить среди
# них только четные. Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.

sasha = list(map(int, input('введите номиналы монет через пробел').split()))
galya = list(map(int, input('введите номиналы монет через пробел').split()))
print(*sorted(filter(lambda x: (x % 2 == 0), (i for i in sasha if galya.count(i)))))
