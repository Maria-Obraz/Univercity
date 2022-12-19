import random


def birthday(iterations: int = 100000, people: int = 23) -> float:
    '''

    :param iterations: количество повторов
    :param people: количество людей
    :return: процент людей с одинаковыми др из people
    '''
    b_day = []
    count_true = 0

    for k in range(iterations):

        for i in range(people):
            d = str(f'{random.randint(1, 28)} {random.randint(1, 12)}')
            if b_day.__contains__(d):
                count_true += 1
                break
            b_day.append(d)

        b_day.clear()

    statement1 = count_true / iterations * 100
    count_pairs = people * (people - 1) / 2
    statement2 = count_pairs / (28 * 12) * 100

    return statement1 % statement2
