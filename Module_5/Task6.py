n = int(input())
i1 = 1
i2 = 1
i = 2
while n >= i2:
    if i2 == n:
        print(i)
        break
    t = i2
    i2 = i2+i1
    i1 = t
    i += 1
if n < i2:
    print(-1)
