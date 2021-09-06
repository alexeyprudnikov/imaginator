import os
import utils
from config import Config


class General:

    def __init__(self, path):

        config = Config()
        self.save_path = f'{path}{config.get("default", "save_path")}'
        self.file_prefix = config.get("default", "file_prefix")

        if os.path.isdir(self.save_path):
            utils.clear_dir(self.save_path, self.file_prefix)
        else:
            utils.create_dir(self.save_path)
