
while True:
    # ввод данных
    x1 = float(input('Введите значение x1: '))

    if abs(x1) >= 1:
        print('\n\nРезультат\n')
        print('Неверное значение x1\n')
        print('-' * 40, '\n')
        continue

    x2 = float(input('Введите значение x2: '))

    if abs(x2) >= 1:
        print('\n\nРезультат\n')
        print('Неверное значение x2\n')
        print('-' * 40, '\n')
        continue

    if x1 >= x2:
        print('\n\nРезультат\n')
        print('Неверное значение границ интервала\n')
        print('-' * 40, '\n')
        continue

    step = float(input('Введите шаг dx: '))
    if step <= 0:
        print('\n\nРезультат\n')
        print('Неверное значение шага интегрирования\n')
        print('-' * 40, '\n')
        continue

    e = float(input('Введите погрешность e: '))

    print('\n\nРезультат:\n')

    i = x1

    left_side = []

    while i < x2:
        if (i == -1 or i == 3):
            print('знаменатель = 0')
            i += step
            continue
        left_side.append((i + 2) / (i ** 2 - 2 * i - 3))
        i += step

    i = x1
    rigth_side = []

    while i < x2:
        n = 0
        summ = 0
        while True:
            fraction = ((-1) ** (n + 1) - 5 / (3 ** (n + 1))) * i ** n
            summ += fraction
            result = summ / 4
            if abs((i + 2) / (i ** 2 - 2 * i - 3) - result) < e:
                break
            n += 1

        rigth_side.append(result)
        i += step

    # вывод значений
    s1 = 'x'
    s2 = 'Левая часть'
    s3 = 'Правая часть'

    print(f'{s1:>6} {s2:>15} {s3:>14}')
    i = 0

    while x1 < x2:
        print(f'{x1:>6.7g}    {left_side[i]:>12.7g}   {rigth_side[i]:>12.7g}')
        i += 1
        x1 += step

    print('\n', '-' * 40, '\n')