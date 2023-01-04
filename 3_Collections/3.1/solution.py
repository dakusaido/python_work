# result: list[int, ...] = [*range(1, (number := int(input('Введите число: '))) + 1, 2)]
#
# print(
#     f'Список из нечётных чисел от 1 до {number}: ',
#     result
# )

# import random
# from benchmark import Benchmark
#
#
# def quicksort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         q = random.choice(nums)
#     l_nums = [n for n in nums if n < q]
#
#     e_nums = [q] * nums.count(q)
#     b_nums = [n for n in nums if n > q]
#     return quicksort(l_nums) + e_nums + quicksort(b_nums)
#
#
# def test_sort(func, point):
#     benc.start(point)
#
#     func(lst)
#
#     return benc.end(point)
#
#
# if __name__ == '__main__':
#     lst = list(map(int, open('numbers.txt', mode='r').readlines()))  # 5000 numbers from 1 to 1000 (inclusive)
#
#     benc = Benchmark()
#
#     print('quick sort\t', test_sort(quicksort, 'quick sort'))  # 62ms
#     print('default sort\t', test_sort(sorted, 'default sort'))  # 15ms
#
#

#
# def main():
#     shop = [
#         ['футболка', 800], ['кроссовки', 5000], ['штаны', 500],
#         ['шорты', 960], ['штаны', 450], ['кепка', 600],
#         ['куртка', 9000], ['кроссовки', 2000], ['штаны', 870]
#     ]
#
#     input_ = input('Название товара: ')
#     cost = 0
#     count = 0
#
#     for item in shop:
#         if item[0] == input_:
#             cost += item[1]
#             count += 1
#
#     print('Кол-во товаров - ', count)
#     print('Общая стоимость - ', cost)
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
#
#     beatles_map.update({'Ringo': 'Drums'})
#     john_instrument = beatles_map.pop('John')
#
#     print(beatles_map)
#     print(john_instrument)
#
#
# if __name__ == '__main__':
#     main()


# from random import sample
#
# unicode_letters_lower = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# unicode_letters_upper = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# unicode_letters = unicode_letters_lower + unicode_letters_upper
# count = 10
#
#
# def main():
#     first_list = sample(unicode_letters, count)
#     second_list = sample(unicode_letters, count)
#
#     first_dict = {index: item for index, item in enumerate(first_list)}
#     second_dict = {index: item for index, item in enumerate(second_list)}
#
#     print(first_dict)
#     print(second_dict)
#
#
# if __name__ == '__main__':
#     main()


