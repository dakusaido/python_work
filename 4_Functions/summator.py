from random import randint
from benchmark import Benchmark


def benc(func):
    def wrapper(*args, **kwargs):
        benc = Benchmark()
        benc.start(func.__name__)

        result = func(*args, **kwargs)

        print(func.__name__, benc.end(func.__name__))

        return result

    return wrapper


@benc
def write_files_in_file(filename: str, files: int):
    with open(filename, 'w') as file1:
        for j in range(files):
            with open(f'numbers{j}', 'r') as file2:
                file1.write(file2.read())

            print(f'write numbers{j} in file - complete')


@benc
def create_files(count: int):
    for j in range(count):
        with open(f'numbers{j}', 'w') as file:
            for _ in range(1_000_000):
                file.write(randint(1, 100).__str__() + ' ')
        print(f'creating numbers{j} - complete')


def reading_file(filename):
    with open(filename) as file:
        string = iter(file.__next__())

    counter = 0

    try:

        while True:
            yield string.__next__()
            counter += 1

    except StopIteration:
        print("Chars of readings: ", counter)


@benc
def get_sum_in_file(filename: str) -> int:
    sum_int: int = 0  # Result
    rub: str = ''  # Read int

    string = reading_file(filename)  # generator of reading file

    try:
        while True:

            input_ = string.__next__()  # Reading

            if input_ == ' ':
                sum_int += int(rub)
                rub = ''  # Reset

            rub += input_  # Add char

    except StopIteration:
        return sum_int


if __name__ == '__main__':
    filename: str = 'numbers.txt'
    benc: Benchmark = Benchmark()

    create_files(100)
    write_files_in_file(filename, 100)

    print("sum - ", get_sum_in_file(filename))

# Output:
#     create_files (16.008842706680298, '16008ms')
#     write_files_in_file (3.2347655296325684, '3234ms')
#     Chars of readings:  291999733
#     get_sum_in_file (15.864644050598145, '15864ms')
#     sum - 5050086683
