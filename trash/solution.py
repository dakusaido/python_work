import os.path
import tempfile
import uuid

class File:
    def __init__(self, path) -> None:
        self.path = path
        self.current_position = 0
        if not os.path.exists(path):
            open(self.path, 'w').close()

    def __str__(self) -> str:
        return self.path

    def __iter__(self) -> object:
        return self

    def __next__(self) -> str:
        with open(self.path, 'r') as f:
            f.seek(self.current_position)
            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')
            self.current_position = f.tell()
            return line

    def __add__(self, obj) -> object:
        new_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())
        return new_file

    def read(self) -> str:
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.path, 'w') as f:
            return f.write(text)