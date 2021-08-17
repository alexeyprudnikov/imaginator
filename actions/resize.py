import os
import glob
from config import Config
from PIL import Image

config = Config()


def create_dir(path):
    try:
        os.makedirs(path, 0o777, True)
    except OSError:
        raise


def clear_dir(path):
    files = glob.glob(f'{path}/{config.get("default", "file_prefix")}*.*')
    for f in files:
        try:
            os.unlink(f)
        except OSError:
            raise


class Resizer:

    def __init__(self, path, dim, value):
        self.path = path
        self.dim = dim  # aspect ratio dimension
        self.value = value
        self.save_path = f'{path}{config.get("default", "save_path")}'
        if os.path.isdir(self.save_path):
            clear_dir(self.save_path)
        else:
            create_dir(self.save_path)

    def resize(self, file_name):
        full_path = f'{self.path}/{file_name}'
        img = Image.open(full_path)
        done = False
        if self.dim == 'width':
            w_percent = (self.value / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            img = img.resize((self.value, h_size), Image.ANTIALIAS)
            done = True
        elif self.dim == 'height':
            h_percent = (self.value / float(img.size[1]))
            w_size = int((float(img.size[0]) * float(h_percent)))
            img = img.resize((w_size, self.value), Image.ANTIALIAS)
            done = True

        if done:
            new_path = f'{self.save_path}/{config.get("default", "file_prefix")}{file_name}'
            img.save(new_path)
