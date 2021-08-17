import sys
import os
from actions.resize import Resizer


actions = [
    '1',
    '2'
]

scalings = [
    '1',
    '2'
]

print('What is the name of your directory?')
#path = input(': ')
path = '/Users/aprudnikov/Documents/Testimages'
try:
    directory = os.listdir(path)
    print(f'directory: {path}')

    print('Select a bulk action')
    action = input('[1 - resize or 2 - crop]: ')
    while action not in actions:
        print("Error: action not presented, please try again")
        action = input('[1 - resize or 2 - crop]: ')

    print('Select scaling base (keeping aspect ratio)')
    scaling = input('[1 - width or 2 - height]: ')
    while scaling not in scalings:
        print("Error: scaling not presented, please try again")
        scaling = input('[1 - width or 2 - height]: ')

    print('Enter base value')
    base_value = int(input(': '))
    while base_value <= 0:
        print("Error: value must be > 0")
        base_value = int(input(': '))

    if action == '1':
        worker = Resizer(path, scaling, base_value)
        count = 0
        for file_name in directory:
            worker.resize(file_name)
            count += 1
        print(f'{count} images proceeded!')

except FileNotFoundError:
    print('Error: Directory not found')

except OSError:
    print('Cann not create target directory')
