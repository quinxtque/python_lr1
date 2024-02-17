from math import pi
from random import uniform

R2 = 10         # внешний радиус
R1 = R2 / 2     # внутренний радиус

# расчет площади фигуры аналитически
S = ((pi * R2 ** 2) / 4) - ((pi * R1 ** 2) / 4) + 2 * R2 ** 2

# расчет площади фигуры методом Монте-Карло
while True:
    N = int(input('Введите количество точек N: '))
    n = 0                                           # количество попавших в фигуру точек

    for i in range(N + 1):
        x = uniform(-R2, R2)
        y = uniform(-R2, R2)

        if (abs(x) <= R2 and abs(y) <= R2 and (x <= 0 and y <= 0 or x >= 0 and y >= 0)) or \
                ((x ** 2 + y ** 2) <= R2 ** 2 and (x ** 2 + y ** 2) >= R1 ** 2 and -R2 < x <= 0 and R2 > y >= 0):
            n += 1
 
    s_monte_carlo = (2 * R2) ** 2 * n / N

    print('\n\nРезультат:\n')

    # Вывод ответа
    print('Метод Монте-Карло       ', f'{s_monte_carlo:<.6g} ед. кв.')
    print('Точное значение         ', f'{S:<.6g} ед. кв.\n')
    print('________________________________________\n')