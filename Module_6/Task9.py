x = input()
len1 = len(x)
if len1 % 2 == 1:
    x1 = x[:(len1//2)+1]
    x2 = x[(len1//2)+1:]
else:
    x1 = x[:(len1 // 2)]
    x2 = x[(len1 // 2):]
print(x2, x1, sep="")
