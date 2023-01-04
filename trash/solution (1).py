import os
import tempfile
class File:
    def __init__(self,path):
        self.path = path;
        with open(self.path, 'a') as file:
            file.write("")

    def __str__(self):
        return os.path.abspath(self.path)

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def write(self, text):
        with open(self.path, 'w') as file:
            file.write(text)

    def __add__(self, obj):
        with open(self.path, 'r') as file1:
            f1 = file1.read()
        with open(obj.path, 'r') as file2:
            f2 = file2.read()
        new_path = os.path.join(tempfile.gettempdir(), tempfile.mktemp())
        with open(new_path, 'w') as file:
            file.write(f1+f2)
            return File(new_path)

    def __getitem__(self, index):
        with open(self.path, 'r') as file:
            mas = file.readlines()
            #mas=f1.split('\n')
            if mas[-1]=='':
                del mas[-1]
            return mas[index]