import os
import tempfile
from json import dumps, load
import argparse

filename = 'storage.data'


def create_json_file(path_to_file: str) -> None:
    with open(path_to_file, 'w', encoding='utf-8') as file:
        file.write('{}')


def get_data(path_to_file: str) -> dict:
    if not os.path.exists(path_to_file):
        create_json_file(path_to_file)
        return {}

    with open(path_to_file, mode='r', encoding='utf-8') as file:
        json_file = load(file)

        return json_file


def save_data(path_to_file: str, data: dict) -> None:
    with open(path_to_file, 'w', encoding='utf-8') as file:
        file.write(dumps(data))


def main(argv):

    data = get_data(storage_path)

    if not argv.value:
        print(', '.join(data.get(argv.key) or []))
        return

    if not data.get(argv.key):
        data[argv.key] = [argv.value]

    else:
        data[argv.key].append(argv.value)

    save_data(storage_path, data)


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), filename)

    parser = argparse.ArgumentParser()

    parser.add_argument("--key")
    parser.add_argument("--value")

    args = parser.parse_args()
    main(args)
