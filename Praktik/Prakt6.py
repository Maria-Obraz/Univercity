import re
f = open('txt/file.txt', 'r', encoding='utf-8')
text = f.readlines()
data = []
for line in text:
    info = re.match(r'(^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w+) (\d+:\d+:\d+)', line)
    if info != None:
        data.append(info[0])
rasp = []
for line in data:
    time = re.search(r'\d+:\d+:\d+', line).group(0)
    number = re.search(r'\d+', line).group(0)
    town = re.search(r'(\w+) (\w+)', line).group(0)
    rasp.append(f'[{time}] - Поезд № {number} {town}')
f = open('txt/nevfile', 'a', encoding='utf-8')
if len (text) != 0:
    f.seek(0)
f.write('\n'.join(rasp))
