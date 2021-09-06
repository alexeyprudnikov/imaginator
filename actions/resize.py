from actions.general import General
from PIL import Image


class Resizer(General):

    def __init__(self, path, dim, val):
        self.path = path
        self.dim = dim  # aspect ratio dimension
        self.val = val

        super().__init__(path)

    def proceed(self, file_name):
        full_path = f'{self.path}/{file_name}'
        img = Image.open(full_path)
        done = False
        if self.dim == 'width':
            w_percent = (self.val / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            img = img.resize((self.val, h_size), Image.ANTIALIAS)
            done = True
        elif self.dim == 'height':
            h_percent = (self.val / float(img.size[1]))
            w_size = int((float(img.size[0]) * float(h_percent)))
            img = img.resize((w_size, self.val), Image.ANTIALIAS)
            done = True

        if done:
            new_path = f'{self.save_path}/{self.file_prefix}{file_name}'
            img.save(new_path)

        return 1
