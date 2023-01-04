import os


class FileReader:

    def __init__(self, path_to_file, encoding='utf-8'):
        self.path_to_file = path_to_file
        self.encoding = encoding
        self.text = ''

    def read(self):

        if not self.check_file():
            self.text = ''

            return self.text

        try:
            with open(
                    file=self.path_to_file,
                    mode='r',
                    encoding=self.encoding
            ) as file:
                self.text = file.read()

        except Exception() as e:
            print(e)

            self.text = ''
            return self.text

        finally:

            return self.text

    def check_file(self):

        if not os.path.exists(self.path_to_file):
            return False

        elif os.path.isdir(self.path_to_file):
            return False

        return True
