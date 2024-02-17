
from math import tan

while True:
    a = float(input('Введите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))

    dx = float(input('Введите шаг интегрирования dx: '))

    print('\n\nРезультат:\n')

    s = 0
    x = a

    while x <= b:
        y = abs(tan(0.2 * x)) + x
        ds = abs(y * dx)
        s += ds
        x += dx

    print(f'Значение интеграла: {s:g}\n')
    print('________________________________________\n')