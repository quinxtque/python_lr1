
from math import cos, sin, pi

g = 9.81                      # ускорение свободного падения м/с2

while True:
    m = float(input('Введите массу тела в килограммах: '))
    alpha = float(input('Введите угол у основания в градусах: ')) * pi / 180
    F = float(input('Введите силу тяги в ньютонах: '))
    k = float(input('Коэффицент трения: '))

    a = F / m - g * (k * cos(alpha) + sin(alpha))

    print(f'Ускорение тела {a:.2f} м/с2\n')
    print('________________________________________\n')
