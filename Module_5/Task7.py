n = int(input())
i1 = 1
i2 = 1
i = 2
while n != i:
    t = i2
    i2 = i2 + i1
    i1 = t
    i += 1
print(i2)
