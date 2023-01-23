# Есть список nums, вернуть true, если какое-либо
# значение встречается в
# списке не менее двух раз, и вернуть false, если каждый элемент различен.

nums = list(map(int, input("Введите числа через пробел ").split()))
print(nums)
f = lambda x: len(x) > len(set(x))
print(f(nums))
