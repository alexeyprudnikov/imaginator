from actions.general import General
from PIL import Image
import pyheif
import os


class Convertor(General):

    def __init__(self, path, ext_from, ext_to):
        self.path = path
        self.ext_from = ext_from
        self.ext_to = ext_to

        super().__init__(path)

    def proceed(self, file_name):
        full_path = f'{self.path}/{file_name}'
        if self.ext_from == 'heic':
            with open(full_path, 'rb') as f:
                data = f.read()
                i = pyheif.read(data)
                img = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        else:
            img = Image.open(full_path)
            if self.ext_from == 'png':
                img.convert('RGB')

        if self.ext_from == self.ext_to:
            return 0

        file_name = os.path.splitext(file_name)[0] + '.' + self.ext_to
        new_path = f'{self.save_path}/{self.file_prefix}{file_name}'
        save_format = 'JPEG' if self.ext_to.lower() == 'jpg' else self.ext_to.upper()
        img.save(new_path, format=save_format)
        return 1
