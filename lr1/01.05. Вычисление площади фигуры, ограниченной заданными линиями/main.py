from math import tan, log, sin
from random import uniform

while True:
    # выбор метода
    print('Для выбора метода интегрирования введите требуемое число:')
    print('1 - метод прямоугольников')
    print('2 - метод трапеций\n')
    method = int(input())

    # ввод данных
    a = float(input('\nВведите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))
    dx = float(input('Введите шаг интегрирования dx: '))

    N = int(input('\nВведите количество точек N: '))

    # вывод ответа
    print('\n\nРезультат:\n')

    if method == 1:
        S = 0
        x = a

        while x <= b:
            y = abs(tan(0.2 * x)) + x - log(x) + sin(x)
            ds = abs(y * dx)
            S += ds
            x += dx

        rectangle_method = S

        print('Метод прямоугольников   ', f'{rectangle_method:<.6g} ед. кв.')
    elif method == 2:
        s = 0
        x = a

        while x <= b:
            y = abs(tan(0.2 * x)) + x + (abs(tan(0.2 * (x + dx))) + x + dx) - (log(x) + sin(x) + (log(x + dx) + sin(x + dx)))
            ds = abs(y / 2 * dx)
            s += ds
            x += dx

        trapezoid_method = s

        print('Метод трапеций          ', f'{trapezoid_method:<.6g} ед. кв.\n')
    else:
        print('Нет такого метода')

    x = a
    min_gx = log(x) + sin(x)
    max_fx = abs(tan(0.2 * x)) + x

    while x <= b:
        if min_gx > log(x) + sin(x):
            min_gx = log(x) + sin(x)
        if max_fx < abs(tan(0.2 * x)) + x:
            max_fx = abs(tan(0.2 * x)) + x
        x += dx

    from_y, to_y = min_gx, max_fx

    n = 0                                       # количество попавших в фигуру точек

    # генерация точек для метода Монте-Карло
    for i in range(N + 1):
        x = uniform(a, b)
        y = uniform(from_y, to_y)

        if log(x) + sin(x) <= y <= abs(tan(0.2 * x)) + x:
            n += 1

    monte_carlo = abs(b - a) * abs(to_y - from_y) * n / N

    # вывод ответа
    print('Метод Монте-Карло       ', f'{monte_carlo:<.6g} ед. кв.\n')
    print('________________________________________\n')