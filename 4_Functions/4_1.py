# def main():
#     with open('numbers.txt', mode='r') as file:
#         print(sum(map(int, file.readlines())))
#
#
# if __name__ == '__main__':
#     main()


import os


def main():
    file_name = 'numbers.txt'
    print(os.path.join(os.path.curdir, file_name))  # .\numbers.txt
    print(os.path.abspath(file_name))               # C:\...\...\...\...\...\numbers.txt


if __name__ == '__main__':
    main()
