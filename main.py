import os
from config import Config
from actions.resize import Resizer
from actions.convert import Convertor


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
    image_types = config.get('default', 'image_types').split(',')
    actions = config.get('default', 'actions').split(',')
    dimensions = config.get('default', 'dimensions').split(',')
    degrees = config.get('default', 'degrees').split(',')

    print('Enter image directory')
    #path = input(': ')
    path = '/Users/aprudnikov/Documents/Testimages'

    try:
        worker = None
        files = []

        print(f'directory: {path}')

        print('Select an action')
        action = get_input_from_list(actions)

        # proceed resize
        if action == 'resize':
            # get files from directory (will also check if directory exists)
            files = [fn for fn in os.listdir(path) if os.path.splitext(fn)[1][1:].lower() in image_types]

            print('Select aspect ratio main dimension')
            dim = get_input_from_list(dimensions)

            print(f'Enter new image {dim}')
            val = get_int_positive_value()

            worker = Resizer(path, dim, val)

        # proceed convert
        if action == 'convert':
            print('Select input extension')
            ext_from = get_input_from_list(image_types)

            files = [fn for fn in os.listdir(path) if os.path.splitext(fn)[1][1:].lower() == ext_from]

            print('Select output extension')
            # exclude ext_from
            image_types.remove(ext_from)
            ext_to = get_input_from_list(image_types)

            worker = Convertor(path, ext_from, ext_to)

        if worker:
            count = 0
            for file_name in files:
                count += worker.proceed(file_name)
            print(f'{count} images proceeded!')

    except FileNotFoundError:
        print('Error: Directory not found')

    except OSError as e:
        print(e.strerror)
        print('Cann not create target directory')

except OSError:
    print('Cann not read config')
