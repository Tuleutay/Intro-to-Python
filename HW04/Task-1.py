# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

# print("{:.{precision}f}".format(math.pi, precision=int(input('Введите точность d 10^{-1} ≤ d ≤10^{-10} '))))

# решение 2
# p = str(3.1415439864863903452352)
# d = input()  # 0.00001
# print(f'math.pi = {p[:len(d)]}')

a = int(input('input tochnost 5'))
pi = 0
for i in range(1, 1000000):
    pi += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
print(str(pi)[:a + 2])  # 3.14159
