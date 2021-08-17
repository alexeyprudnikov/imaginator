from configparser import ConfigParser


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class Config:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')

    def get(self, section, option):
        return self.config.get(section, option)
