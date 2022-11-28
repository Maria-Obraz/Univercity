import random
def MontyHoll(iterations):
    vary = 0
    not_vary = 0
    for i in range(iterations):
        a = [0,0,1] #варианты дверей
        choise = random.randint(0,2) #игрок выбирыет дверь
        a.pop(choise) #дверь игрока открывается
        a.remove(0) #едущий открывает дверь
        if a[0] == 1: #если игрок хочет поменять выбор
            vary += 1
        else:  #иначе оставить свой
            not_vary += 1
            return f'agree: {vary/iterations * 100}\nnot agree: {not_vary/iterations * 100}'
