import os
from config import Config
from actions.resize import Resizer


# proceed input as integer by list index (starting from 1) and return value of index
def get_input_from_list(input_list):
    input_label = ', '.join([f'{i + 1} - {v}' for i, v in enumerate(input_list)])
    while True:
        try:
            value = int(input(f'{input_label}: '))
            if value not in [i + 1 for i, v in enumerate(input_list)]:
                raise ValueError
            break
        except ValueError:
            print('Error: input value not presented, please try again')
    return input_list[value - 1]


def get_int_positive_value():
    while True:
        try:
            value = int(input(': '))
            if value < 1:
                raise ValueError
            break
        except ValueError:
            print("Error: value must be > 0")
    return value


try:

    config = Config()
    actions = config.get('default', 'actions').split(',')
    dimensions = config.get('default', 'dimensions').split(',')

    print('Enter image directory')
    path = input(': ')

    try:
        # get files from directory (will also check if directory exists)
        image_types = config.get('default', 'image_types').split(',')
        files = [fn for fn in os.listdir(path) if fn.split(".")[-1] in image_types]

        print(f'directory: {path}')

        print('Select an action')
        action = get_input_from_list(actions)

        print('Select aspect ratio main dimension')
        dim = get_input_from_list(dimensions)

        print(f'Enter new image {dim}')
        val = get_int_positive_value()

        # proceed
        if action == 'resize':
            worker = Resizer(path, dim, val)
            count = 0
            for file_name in files:
                worker.resize(file_name)
                count += 1
            print(f'{count} images proceeded!')

    except FileNotFoundError:
        print('Error: Directory not found')

    except OSError as e:
        print(e.strerror)
        print('Cann not create target directory')

except OSError:
    print('Cann not read config')
