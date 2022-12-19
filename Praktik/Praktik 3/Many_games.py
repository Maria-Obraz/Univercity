import random

def choose_continue_game(wor: list[str]) -> bool:
    '''

    :param wor: список слов для игры
    :return: выбор пользователя продолжения игры
    '''
    if len(wor) == 0:
        return False

    choice = input('Хотите сыграть еще? да/нет ')
    if choice == 'да':
        return True
    if choice == 'нет':
        return False
    choose_continue_game(wor)

def find_worrd(wor: list[str]) -> str:
    '''

    :param wor: список слов для игры
    :return: случайное слово из списка
    '''
    print(wor)
    worrd = random.choice(wor)
    wor.remove(worrd)
    return worrd
