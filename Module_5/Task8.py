i1 = int(input())
i2 = int(input())
s = 1
s_max = 1
while i2 != 0:
    if i1 == i2:
        s += 1
        if s > s_max:
            s_max = s
        else:
            s = 1
            t = i2
            i2 = int(input())
            i1 = t
print(s_max)

