from math import log


def main():
    """
        Добавленный в Python 3.8 моржовый оператор (:=),
        формально известен как оператор присваивания выражения.
        Он дает возможность присвоить переменные в выражении,
        включая переменные, которых еще не существует.

        Здесь необходимое число находится путем централизации.
        Еще можно было это сделать рекурсией.
        Максимальное количество попыток - 7
    """

    computer_number = 50
    i = 2
    computer_text = lambda number: f"Твое число больше, равно или меньше, чем число {number}?\n"

    while (_input := input(computer_text(computer_number)).lower()) != "равно":
        if _input == 'меньше':
            computer_number -= 100 // (2 ** i) + log(i, 7).__int__()
        else:
            computer_number += 100 // (2 ** i) + log(i, 7).__int__()
        i += 1
    else:
        print('I win!', i - 2)


if __name__ == '__main__':
    main()
