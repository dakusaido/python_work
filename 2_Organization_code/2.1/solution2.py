from sys import argv


def main(args):
    count = int(args[1])
    for i in range(1, count + 1):
        print(' ' * (count - i) + '#' * i)


if __name__ == '__main__':
    main(argv)
