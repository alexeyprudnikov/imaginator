import os
from config import Config
from actions.resize import Resizer


def proceed_input_from_list(input_list):
    error_label = 'Error: input value not presented, please try again'
    input_label = ' or '.join([f'{idx + 1} - {val}' for idx, val in enumerate(input_list)])
    while True:
        try:
            input_value = int(input(f'{input_label}: '))
            while input_value not in [idx + 1 for idx, val in enumerate(input_list)]:
                print(error_label)
                input_value = int(input(f'{input_label}: '))
            return input_value
        except ValueError:
            print(error_label)


try:

    config = Config()
    actions = config.get('default', 'actions').split(',')
    dimensions = config.get('default', 'dimensions').split(',')

    print('Enter image directory')
    path = input(': ')
    try:
        print(f'directory: {path}')

        print('Select an action')
        action = proceed_input_from_list(actions)

        print('Select aspect ratio main dimension')
        dim = proceed_input_from_list(dimensions)

        print(f'Enter new image {"width" if dim == "1" else "height"}')
        value = int(input(': '))
        while value <= 0:
            print("Error: value must be > 0")
            value = int(input(': '))

        # get files from directory
        image_types = config.get('default', 'image_types').split(',')
        files = [fn for fn in os.listdir(path) if fn.split(".")[-1] in image_types]

        # proceed
        if action == 1:
            worker = Resizer(path, dim, value)
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
