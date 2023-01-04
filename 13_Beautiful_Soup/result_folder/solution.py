import re

from bs4 import BeautifulSoup
from typing import List, Set

__all__ = ['parse']


def get_html(path_to_file: str):
    with open(file=path_to_file, mode='r', encoding='utf-8') as file:
        html = file.read()

    return html


def get_count_imgs(width: int, soup: BeautifulSoup) -> int:
    images = soup.find_all('img')

    return len(
        list(
            filter(
                lambda width_: width_ >= width,
                map(lambda img: int(img.get('width') or '0'), images)
            )
        )
    )


def get_count_all_headers(words: Set[str], soup: BeautifulSoup) -> int:
    headers = soup.find_all(re.compile('^h[1-6]$'))

    return len(
        list(
            filter(
                lambda soup_text: soup_text.text[0] in words, headers
            )
        )
    )


def get_max_len_links(soup: BeautifulSoup) -> int:
    links = soup.find_all('a')

    parents = set([link.parent for link in links])
    result = 1
    counter = 1

    for parent in parents:
        childrens = [child.name for child in parent.childGenerator() if child.name]

        result = max(counter, result)
        counter = 1
        for children_first, children_second in zip(childrens, childrens[1:]):
            if children_first == children_second == 'a':
                counter += 1

                continue

            result = max(counter, result)
            counter = 1

    return result


def get_lists(soup: BeautifulSoup) -> int:
    lists = soup.find_all(re.compile('^[ou]l$'))
    lists_names = {'ul', 'ol', 'li'}
    # definition_lists = {'dl', 'dt', 'dd'}  # Definition lists are also lists!

    len_lists = lists.__len__()

    for list_ in lists:
        parent = list_.findParent(lists_names)

        if parent:
            if parent.name in lists_names:
                len_lists -= 1

    return len_lists


def parse(path_to_file: str) -> List[int]:
    html = get_html(path_to_file=path_to_file)
    soup = BeautifulSoup(html, 'lxml').find('div', id="bodyContent")

    imgs = get_count_imgs(width=200, soup=soup)
    headers = get_count_all_headers(words={'E', 'T', 'C'}, soup=soup)
    linkslen = get_max_len_links(soup=soup)
    lists = get_lists(soup=soup)

    return [imgs, headers, linkslen, lists]
