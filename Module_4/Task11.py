x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())
if (((x+y) % 2 == 0) and ((x2+y2) % 2 == 0)) or (((x+y) % 2 == 1) and ((x2+y2) % 2 == 1)):
    print("ДА")
else:
    print("Нет")
