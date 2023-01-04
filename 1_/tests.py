# from sys import argv
#
#
# def main(args: list[str, ...] | tuple[str, ...]) -> None:
#     print(
#         args[1].__len__(),
#         args[1].lower()
#     )
#
#
# if __name__ == '__main__':
#     main(argv)


# def main():
#     string: str = input('Введите текст: ')
#     result: list[str, ...] = list(map(lambda s: s * 10, string))
#     print(*result, sep='\n')
#
#
# if __name__ == '__main__':
#     main()


# alphabet = 'абвгдеёжзи'
#
#
# def main():
#     print(
#         alphabet[:],            # Copy
#         alphabet[::-1],         # Reverse
#         alphabet[::2],          # Every second element of the string
#         alphabet[1::2],         # Every second element of the string after the first
#         alphabet[:4],           # All elements up to the fifth
#         alphabet[2:6],          # All elements in the index range from 2 to 6 (not including 6)
#         alphabet[-3:],          # The last three elements of the string
#         alphabet[4:2:-1],       # All elements in index range 3 to 4 in reverse order
#         sep='\n'
#     )
#
#
# if __name__ == '__main__':
#     main()


# print(*input("Введите число: "), sep='\n')


# year = int(input("Введите год: "))
# print(
#     f"Год{'' if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0 else ' не'} високосный"
# )

# import re
#
# pattern = re.compile("^(https)+(/documentlibrary/)?")
# print(re.match(pattern, "https://site/subsite/documentlibrry/Sales.rdl"))


# def main():
#     result = [f'{i} ** 5 = {i ** 5}' for i in range(1, int(input('Введите число: ')) + 1, 2)]
#     print(*result, sep='\n')
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     while input('Введите пароль: ') != "qwerty123":
#         print('Неверный пароль! Попробуйте ещё раз.')
#     else:
#         print('Пароль верный!')
#
#
# if __name__ == '__main__':
#     main()

