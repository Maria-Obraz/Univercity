import random
a = [0, 1, 0]
def monty_hall_wic

def monty_hall_wc
    random.shuffle(a)
    first_a = random.randrange(len(a))
    for i in range(len(a)):
    if i != first_a and a[i] == 0:
        host_a = i
        break
    for i in range(len(a)):
    if != first_a and i != host_a:
        return a[i]
a = ['0', '1', '0']
N = 100000
win = 0
for _ in range(N):
    resul =