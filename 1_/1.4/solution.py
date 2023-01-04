from random import randint


def main():

    """
        Добавленный в Python 3.8 моржовый оператор (:=),
        формально известен как оператор присваивания выражения.
        Он дает возможность присвоить переменные в выражении,
        включая переменные, которых еще не существует.
    """

    random_number = randint(1, 10)
    count = 1
    while (number := int(input('Введите число: '))) != random_number:
        print(f'Число {"меньше" if number < random_number else "больше"}'
              f', чем нужно. Попробуйте ещё раз!')
        count += 1
    else:
        print('Вы угадали! Число попыток: ', count)


def second_main():

    """
        Для Python 3.7 и ниже
    """

    random_number = randint(1, 10)
    count = 1

    number = int(input('Введите число: '))

    while number != random_number:
        print(f'Число {"меньше" if number < random_number else "больше"}'
              f', чем нужно. Попробуйте ещё раз!')

        count += 1
        number = int(input('Введите число: '))
    else:
        print('Вы угадали! Число попыток: ', count)


if __name__ == '__main__':
    main()
    second_main()
