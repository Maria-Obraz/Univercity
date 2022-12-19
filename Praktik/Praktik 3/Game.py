import re

def choose_complexity() -> int:
    '''
    Меню выбора сложности
    :return: количество попыток игрока
    '''
    c = input('\nВыберите сложность: 1 - 3 жизни, 2 - 5 жизней, 3 - 7 жизней ')
    return (2 * int(c) + 1) if c == '1' or c == '2' or c == '3' else choose_complexity()

def check_input(wor: str) -> str:
    '''
    Проверка ввода правильных символов
    :param wor: загаданное слово
    :return: введенное слово
    '''
    n = input('\nВведите букву или слово: ')
    if re.findall(r'[а-яА-Я]', n) == []:
        check_input(wor)
    return n

def play(wor: str) -> int:
    '''
    Описание процесса игры. Проверка возможных вариантов победы и проигрыша
    :param wor: загаданное слово
    :return: количество попыток - рекорд
    '''
    max_attemps = choose_complexity()
    attemps = max_attemps

    print_wor = []
    for i in range(len(wor)):
        print_wor.append('\u25A0')
    print(*print_wor)

    while attemps > 0:
        n = check_input(wor)

        if len(n) == 1:
            if n in wor:
                for i in range(len(wor)):
                    if wor[i] == n:
                        print_wor[i] = n
                print('Вы угадали')
                print(*print_wor)

                if not print_wor.__contains__('\u25A0'):
                    print(f'Вы выиграли!')
                    return max_attemps - attemps
            else:
                attemps -= 1
                print(f'Вы не угадали. Ваши жизни {attemps}')
                print(*print_wor)

        elif n == wor:
            print(f'Вы выиграли!')
            return max_attemps - attemps
        else:
            attemps -= 1
            print(f'Вы не угадали. Ваши жизни {attemps}')
            print(*print_wor)

    print(f'Вы проиграли! Слово было {wor}')
    return max_attemps - attemps
