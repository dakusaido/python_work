from sys import argv


def main(args):
    a = int(args[1])
    b = int(args[2])
    c = int(args[3])

    if (a + b + c) == 0:
        print(c // a,
              1,
              sep='\n')
        return

    elif (a - b + c) == 0:
        print(
            -c // a,
            -1,
            sep='\n'
        )
        return

    discriminant = (b ** 2) - (4 * a * c)
    print(
        int((-b + discriminant ** 0.5) / (2 * a)),
        int((-b - discriminant ** 0.5) / (2 * a)),
        sep='\n'
    )


if __name__ == '__main__':
    main(argv)