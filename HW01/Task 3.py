#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])
# для всех значений предикат.
x=None
y=None
z=None
s = not(x or y or z)
t = not(x) and not(y) and not(z)
if s==t:
    print('True')
else:
    print('False')
