# def main():
#     square_lst = lambda: [x ** 2 for x in range(10)]
#     print(square_lst())
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     population_koefs = [1.1, -0.12, 3.12, -0.99, -2, 22, 2.88, -2.92, 1.16, 4.2]
#
#     lst = [x if x > 0 else 0 for x in population_koefs]
#
#     print(lst)
#
#
# if __name__ == '__main__':
#     main()


# with open('numbers.txt', 'w') as file1:
#     for j in range(100):
#         with open(f'numbers{j}', 'r') as file2:
#             file1.write(file2.read())
#         print(f'numbers{j} complete')

# from random import randint
#
# for j in range(10, 100):
#     with open(f'numbers{j}', 'w') as file:
#         for _ in range(1_000_000):
#             file.write(randint(1, 100).__str__() + ' ')
#     print(f'numbers{j} complete')

# def get_string(filename):
#     with open(filename) as file:
#         string = iter(file.__next__())
#
#     counter = 0
#
#     try:
#
#         while True:
#
#             yield string.__next__()
#             counter += 1
#
#     except StopIteration:
#         print(counter)
#
#
# def get_sum_in_file(filename: str) -> int:
#     sum_int = 0
#     rub = ''
#
#     string = get_string(filename)
#
#     try:
#         while True:
#
#             input_ = string.__next__()
#
#             if input_ == ' ':
#                 sum_int += int(rub)
#                 rub = ''
#
#             rub += input_
#
#     except StopIteration:
#         return sum_int
#
#
# filename = 'numbers.txt'
#
# from benchmark import Benchmark
#
# benc = Benchmark()
#
# benc.start('first')
#
# print(get_sum_in_file(filename))
#
# result = benc.end('first')
#
# print(result)

# 1767581482

# 291993484
# 5049788943
# (19.214417457580566, '19214ms')


# 6888890
# 499999500000
# (2.7007553577423096, '2700ms')


# 499_999_500_000

# with open('number.txt', 'w') as file:
#     for i in range(1_000_000):
#         file.write(i.__str__() + ' ')


# to_convert_string = lambda lst: list(map(str, lst))
#
# lst = list(range(10))
#
# print(to_convert_string(lst))


import os
import tempfile
import functools

path_to_logger = lambda name: os.path.join(tempfile.gettempdir(), name)


def create_logger(path, printing: bool = False) -> bool:
    if printing:
        print(f"Creating {path}")

    try:
        open(path, mode='w').close()

    except Exception() as e:
        print(e)
        return False

    finally:
        if printing:
            print(f'Success creating {path}')

        return True


def write_to_logger(result: str, path, mode='a', encoding='utf-8', printing=False) -> bool:

    if printing:
        print(f"Writing to {path}")

    try:
        with open(path, mode=mode, encoding=encoding) as file:
            file.write(result + '\n')

    except Exception() as e:
        print(e)
        return False

    finally:
        if printing:
            print(f'Success writing to {path}')

        return True


def logger(path=None, **logger_kwargs):

    def _log(func):
        path_ = path or path_to_logger('log.txt')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            if not os.path.exists(path_):
                if not create_logger(path_, printing=logger_kwargs.get('printing')):
                    return result

            if not write_to_logger(result.__str__(), path_, printing=logger_kwargs.get('printing')):
                return result

            return result

        return wrapper

    return _log


log = logger()  # It's also function, but with default attribute [path=None]


def summator(nums_list):
    return sum(nums_list)


if __name__ == '__main__':
    logger_name = 'logger'
    logger_format = ''

    num_list = [1, 2, 3, 4]

    # Default writing
    print(
        log(summator)(num_list)  # 10
    )

    # Writing with correct path
    print(                                          # Creating logger
        logger(                                     # Success creating logger
            path=logger_name + logger_format,       # Writing to logger
            printing=True                           # Success writing to logger
        )                                           # 10
        (summator)(num_list)
    )
