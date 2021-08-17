import os
import glob


def create_dir(path):
    try:
        os.makedirs(path, 0o777, True)
    except OSError:
        raise


def clear_dir(path, prefix):
    files = glob.glob(f'{path}/{prefix}*.*')
    for f in files:
        try:
            os.unlink(f)
        except OSError:
            raise
