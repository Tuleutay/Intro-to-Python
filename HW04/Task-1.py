# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
print("{:.{precision}f}".format(math.pi, precision=int(input('Введите точность d 10^{-1} ≤ d ≤10^{-10} '))))
