a = int(input())
h = a // 100
d = (a - (h*100)) // 10
e = a % 10
if(h < d) and (d < e) and (h < e):
    print("Да")
else:
    print("Нет")
