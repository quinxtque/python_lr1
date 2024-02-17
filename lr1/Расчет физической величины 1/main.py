
from math import sin, pi, cos

g = 9.81               # ускорение свободного падения, м/с2

alpha = float(input('Введите угол вектора скорости в градусах: ')) * pi / 180
v0 = float(input('Введите начальную скорость тела в м/с: '))

x_max = v0 * cos(alpha) * (2 * v0 * sin(alpha)) / g
y_max = (v0 ** 2 * sin(alpha) ** 2) / (2 * g)

print('\n\nРезультат:\n')

print(f'Дальность полета тела {x_max:g} м')
print(f'Наибольшая высота подъема тела {y_max:g} м\n')

print('________________________________________\n')


