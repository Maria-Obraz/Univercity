a = int(input())
t = a // 1000
h = (a % 1000) // 100
d = (a % 100) // 10
e = a % 10
if(t == e) and (h == d):
    print("Да")
else:
    print("Нет")
