
R1 = 5          # внутренний радиус
R2 = R1 * 2     # внешний радиус

while True:
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))

    print('\n\nРезультат:\n')

    if -R2 >= x >= 0 and 0 <= y <= R2 and R1 ** 2 <= x ** 2 + y ** 2 <= R2 ** 2:
        print('Область попадания А')

    if -R1 <= x <= R1 and -R1 <= y <= R1 and (x <= 0 and y >= 0 or x >= 0 and y <= 0) and \
            x ** 2 + y ** 2 <= R1 ** 2:
        print('Область попадания B')

    if -R2 <= x <= R2 and -R2 <= y <= R2 and (x <= 0 and y <= 0 or x >= 0 and y >= 0):
        print('Область попадания C')

    if 0 <= x <= R2 and -R2 <= y <= 0 and R1 ** 2 <= x ** 2 + y ** 2 <= R2 ** 2:
        print('Область попадания D')

    if 0 < x and x > R2 and 0 < y and y > R2 or x < 0 and y < 0 and x ** 2 + y ** 2 > R2 ** 2 or \
            x < 0 and y < 0 and x < -R2 and y < -R2 or x > 0 and y < 0 and x ** 2 + y ** 2 > R2 ** 2:
        print('Область попадания E')

    print('\n________________________________________\n')


