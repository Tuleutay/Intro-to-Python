# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
from random import shuffle

numbers = [1, 2, 3, 4, 5]
print(numbers)
shuffle(numbers)
print(numbers)