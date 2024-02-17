
R2 = 10
R1 = R2 / 2

while True:
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))

    print('\n\nРезультат:\n')

    if x > R1 or y > R1:
        print('Область попадания E\n')
    elif abs(x) < R1 and abs(y) < R1 and (x < 0 and y < 0 or x > 0 and y > 0):
        print('Область попадания С\n')
    elif (x ** 2 + y ** 2) < R1 ** 2 and (x ** 2 + y ** 2) > R2 ** 2 and x < 0 and y > 0:
        print('Область попадания А\n')
    elif (x ** 2 + y ** 2) < R1 ** 2 and (x ** 2 + y ** 2) > R2 ** 2 and x > 0 and y < 0:
        print('Область попадания D\n')
    elif (x ** 2 + y ** 2) < R2 ** 2 and (x < 0 and y > 0 or x > 0 and y < 0):
        print('Область попадания B\n')
    # пересечение B C
    elif abs(x) < R2 and y == 0 or abs(y) < R2 and x == 0:
        print('Область попадания B и C\n')
    # пересечение A B
    elif (x ** 2 + y ** 2) == R2 ** 2 and x < 0 and y > 0:
        print('Область попадания A и B\n')
    # пересечение B D
    elif (x ** 2 + y ** 2) == R2 ** 2 and x > 0 and y < 0:
        print('Область попадания B и D\n')
    # пересечение A C
    elif x < 0 and R2 < abs(x) < R1 and y == 0 or y > 0 and R2 < abs(y) < R1 and x == 0:
        print('Область попадания A и C\n')
    # пересечение C D
    elif x > 0 and R2 < abs(x) < R1 and y == 0 or y < 0 and R2 < abs(y) < R1 and x == 0:
        print('Область попадания C и D\n')
    # пересечение B C D
    elif abs(x) == R2 and y == 0 and x > 0 or abs(y) == R2 and y < 0 and x == 0:
        print('Область попадания B, C и D\n')
    # пересечение A B C
    elif abs(x) == R2 and y == 0 and x < 0 or abs(y) == R2 and y > 0 and x == 0:
        print('Область попадания A, B и C\n')
    # пересечение С D E
    elif x == R1 and y == 0 or y == -R1 and x == 0:
        print('Область попадания C, D, E\n')
    # пересечение A C E
    elif x == R1 and y == 0 or y == R1 and x == 0:
        print('Область попадания A, C, E\n')
    # пересечение C E
    elif abs(x) == R1 and 0 < abs(y) <= R1 or abs(y) == R1 and 0 < abs(x) <= R1:
        print('Область попадания C и E\n')
    # пересечение A E
    elif (x ** 2 + y ** 2) == R1 ** 2 and x < 0 < y:
        print('Область попадания A и E\n')
    # пересечение D E
    elif (x ** 2 + y ** 2) == R1 ** 2 and y < 0 < x:
        print('Область попадания D и E\n')

    print('________________________________________\n')







