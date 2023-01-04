from sys import argv


def sum_digits(*args):
    return sum(map(int, args[1]))


if __name__ == '__main__':
    print(sum_digits(*argv))
