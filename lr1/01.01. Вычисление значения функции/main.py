
from math import cos, sqrt, tan, log, sin

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
print('\n')

while True:
    x = float(input('x: '))

    if x <= a:
        y = sqrt(-x) * cos(x)
    elif a < x < b:
        y = tan(0.2 * x) + x
    else:
        y = log(x) + sin(x)

    print(f'y: {y:g}\n')






