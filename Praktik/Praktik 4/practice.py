import re

def read_file(name: str) -> list[str]:
    '''

    :param name: путь к файлу чтения
    :return: список отсортированных уникальных слов без спец симоволов
    '''
    a = open(name, 'r')
    text = a.read() #чтение из файла
    text = re.sub(r'[^\w\s]', '', text) #удаление пунктуации
    text = text.lower() #перевод в нижний регистр
    wor = text.split() #разделение
    wor = list(set(wor)) #удаление повторов
    wor.sort() #сортировка
    a.close()
    return wor

def save_file(name: str, words: list[str]) -> None:
    '''

    :param name: путь к файлу записи
    :param words: список слов
    :return:
    '''
    a = open(name, 'r')
    text = a.read()
    if len(text) != 0:
        a.seek(0)
        a.close()
        return 0

    a = open(name, 'a')
    a.write(f'Всего уникальных слов: {str(len(words))} \n================\n')
    a.write('\n'.join(words))
    a.close()

words = read_file('data.txt')
save_file("count.txt", words)
