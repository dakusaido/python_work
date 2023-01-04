# from re import findall, compile
#
# pattern = compile('[@!#№$%&]?')
#
#
# def main():
#     string = input('Введите строку: ') or "$Ан@лиз# д@нных%на% №Python!"
#
#     print(
#         'Количество специальных символов: ',
#         ''.join(findall(pattern, string)).__len__()
#     )
#
#
# if __name__ == '__main__':
#     main()

# from re import compile
#
# pattern = compile(r'[!?,.]?')
#
# text = """
#             Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
#             Aenean commodo ligula eget dolor. Aenean massa.
#             Cum sociis natoque penatibus et
#         """
#
#
# def get_words(_line: str) -> list[str, ...]:
#     clear_string = pattern.sub('', text)  # Очищает строку от запятых, точек, восклицательных и вопросительных знаков
#     words = clear_string.split()  # Получаем список слов
#
#     return words
#
#
# def main():
#     print(get_words(text))
#
#
# if __name__ == '__main__':
#     main()

from re import compile, match

pattern = compile('^[а-яА-ЯёЁ][а-яА-ЯёЁ]{1,20}$')


def print_person(username: str, age=None, line_: str = 'Добро пожаловать') -> str:
    if not match(pattern, username):
        return 'Неверный ввод. Введите имя без цифр'

    return f'Имя: {username}\n' \
           f'Возраст: {age}\n' \
           f'{line_}, {username}!'


def main():
    print(print_person('Вася2'))
    print(print_person('Вася'))
    print(print_person('Петя', 25))
    print(print_person('Катя', line_='Привет'))


if __name__ == '__main__':
    main()
