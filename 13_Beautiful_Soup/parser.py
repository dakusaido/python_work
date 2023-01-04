# from bs4 import BeautifulSoup
# from csv import writer
from solution import parse


# def main():
#     from os import listdir
#     from os.path import isfile, join
#
#     path = './soup_sample/wiki'
#
#     files = [f for f in listdir(path) if isfile(join(path, f))]
#
#     counter = 0
#     len_files = files.__len__()
#
#     with open('result.csv', 'w', encoding='utf-8') as file_:
#         csv_writer = writer(file_)
#         for file in files:
#             html = get_html(f'./soup_sample/wiki/{file}')
#             soup = BeautifulSoup(html, 'lxml').find('div', id="bodyContent")
#
#             imgs = get_count_imgs(200, soup)
#             headers = get_count_all_headers(words={'E', 'T', 'C'}, soup=soup)
#             links = get_max_len_links(soup)
#             lists = get_lists(soup)
#
#             csv_writer.writerow([file, imgs, headers, links, lists])
#
#             counter += 1
#
#             print(round(counter / len_files * 100, 2), '%...')


if __name__ == '__main__':
    print(parse('./soup_sample/wiki/Stone_Age'))
