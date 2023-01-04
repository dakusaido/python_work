# import os
#
#
# def create_file(path) -> bool:
#
#     try:
#         open(path).close()
#
#     except FileExistsError as e:
#         ...
#
#         return False
#
#     except PermissionError as e:
#         ...
#
#         return False
#
#     except Exception() as e:
#         print(e)
#
#         return False
#
#     finally:
#         return True
#
#
# def write_file(text: str, path, mode='w', encoding='utf-8', separator='\n') -> bool:
#
#     if os.path.isdir(path):
#         print(f'[PermissionError] ({path}) is a folder')
#
#         return False
#
#     if mode == 'a':
#         if not os.path.exists(path):
#             if not create_file(path):
#                 return False
#
#     try:
#         with open(
#                 file=path,
#                 mode=mode,
#                 encoding=encoding
#         ) as file:
#             file.write(text + separator)
#
#     except Exception() as e:
#         print(e)
#         return False
#
#     finally:
#         return True
#
#
# def main():
#     input_ = input("Введите текст -: ")
#     path = r'C:\Users\Lenovo\Desktop\python_work\6_OOP\6_5\log'
#
#     print(write_file(input_, path, mode='a'))  # True
#
#
# if __name__ == '__main__':
#     main()


##############################################################

# class LengthError(BaseException):
#
#     def __init__(self, message):
#         self.message = message
#
#
# def main():
#     sum_int = 0
#
#     with open('names.txt', mode='r', encoding='utf-8') as file:
#
#         while line := file.readline():
#             if len(line) < 6:
#                 raise LengthError(f'[{line[:-1]}] length should not be less than five [len={len(line) - 1}]')
#
#             sum_int += len(line)
#
#     print(sum_int)
#
#
# if __name__ == '__main__':
#     main()


##############################################################

import os


class FileReader:

    def __init__(self, path_to_file, encoding='utf-8'):
        self.path_to_file = path_to_file
        self.encoding = encoding
        self.text = ''

    def read(self):

        if not self.check_file():
            self.text = ''

            return self.text

        try:
            with open(
                    file=self.path_to_file,
                    mode='r',
                    encoding=self.encoding
            ) as file:
                self.text = file.read()

        except Exception() as e:
            print(e)

            self.text = ''
            return self.text

        finally:

            return self.text

    def check_file(self):

        if not os.path.exists(self.path_to_file):
            return False

        elif os.path.isdir(self.path_to_file):
            return False

        return True


if __name__ == '__main__':
    reader = FileReader('names.txt')
    text = reader.read()
    print(text)