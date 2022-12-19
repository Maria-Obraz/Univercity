import os

def get_words(path: str= os.path.dirname(__file__) + '\\' + 'wor.txt') -> list[str]:
    '''
    Ошибка если не удалось прочитать файл
    :param path: путь файла
    :return: список слов для игры
    '''
    if not check_file(path):
        print('Ошибка!')
    a = open(path, 'r+', encoding='utf-8')
    text = a.readlines()
    wor = str(*text).split()
    a.close()
    return wor

def write_record(record: int, file: str= os.path.dirname(__file__) + '\\' + 'record.txt') -> None:
    '''
    Ошибка если не удалось прочитать файл
    :param record: рекорд игрока
    :param file: путь к файлу в который записывается рекорд
    :return:
    '''
    if not check_file(file):
        print('Ошибка!')
    a = open(file, 'r+', encoding='utf-8')
    old_record = a.read()
    if record < int(old_record):
        print('Новый рекорд!')
        a.seek(0)
        a.write(str(record))
    a.close()

def check_file(filename: str) -> bool:
    '''

    :param filename: путь к файлу
    :return: есть ли ошибка
    '''
    error = True
    try:
        text = open(filename, 'r', encoding='utf-8')
    except KeyboardInterrupt:
        print('Вы отменили операцию')
    except IOError:
        print('Невозможно прочитать файл')
    except:
        print('Произошла непредвиденная ошибка')
    else:
        error = False

    return not error