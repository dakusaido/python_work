from math import sqrt


class Primes:
    __start: int = 2
    __end: int = 2
    __iterable_number: int = 2

    def __init__(self, end: int, start: int = 2):
        self.__start = start if isinstance(start, int) else self.__start
        self.__iterable_number = start if isinstance(start, int) else self.__start
        self.__end = end if isinstance(end, int) else self.__end

    def __iter__(self):
        return self

    @staticmethod
    def is_prime(num: int) -> bool:
        for i in range(2, round(sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True

    def __next__(self):

        while self.__iterable_number <= self.__end:

            self.__iterable_number += 1

            if self.is_prime(self.__iterable_number - 1):
                return self.__iterable_number - 1

        raise StopIteration


if __name__ == '__main__':
    prime_nums = Primes(50)
    for i_elem in prime_nums:
        print(i_elem, end=' ')
