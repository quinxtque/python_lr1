
R1 = 5          # внутренний радиус
R2 = R1 * 2     # внешний радиус

while True:
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))

    print('\n\nРезультат:\n')

    if y == 0:
        if x == -R2:
            print('Области попадания A, C, E\n')

        elif x == -R1:
            print('Области попадания A, B, C\n')

        elif x == R1:
            print('Области попадания C, B, D\n')

        elif x == R2:
            print('Области попадания C, D, E\n')

        elif -R2 < x < -R1:
            print('Области попадания A, C\n')

        elif -R1 < x < R1:
            print('Области попадания B, C')

        elif R1 < x < R2:
            print('Области попадания C, D\n')

    elif x == 0:
        if y == -R2:
            print('Области попадания C, D, E\n')

        elif y == -R1:
            print('Области попадания C, B, D\n')

        elif y == R1:
            print('Области попадания A, B, C\n')

        elif y == R2:
            print('Области попадания A, C, E\n')

        elif -R2 < y < -R1:
            print('Области попадания C, D\n')

        elif -R1 < y < R1:
            print('Области попадания B, C\n')

        elif R1 < y < R2:
            print('Области попадания A, C')

    elif x == 0 and y == 0:
        print('Области попадания B, C\n')

    elif -R1 < x < 0 and 0 < y < R1 or 0 < x < R1 and -R1 < y < 0:
        if x ** 2 + y ** 2 < R1 ** 2:
            print('Область попадания B\n')

    elif -R2 < x < 0 and 0 < y < R2:
        if -R1 ** 2 < x ** 2 + y ** 2 < R2 ** 2:
            print('Область попадания А\n')

        elif x ** 2 + y ** 2 == R2 ** 2:
            print('Области попадания A, E\n')

    elif 0 < x < R2 and 0 < y < R2 or -R2 < x < 0 and -R2 < y < 0:
        print('Область попадания C\n')

    elif 0 < x < R2 and -R2 < y < 0:
        if R1 ** 2 < x ** 2 + y ** 2 < R2 ** 2:
            print('Область попадания D\n')

    elif x > 0 and y > 0 and (x == R2 and y < R2 or y == R2 and x < R2) or x < 0 and y < 0 and (x == -R2 and y > -R2 or y == -R2 and x > -R2):
        print('Области попадания C, E\n')

    else:
        print('Область попадания E\n')

    print('________________________________________\n')
















