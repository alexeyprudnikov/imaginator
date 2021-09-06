from general import General
from PIL import Image


class Rotator(General):

    def __init__(self, path, degree):
        self.path = path
        self.degree = degree

        super().__init__(path)
