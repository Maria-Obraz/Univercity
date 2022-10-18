lst1 = [int(s) for s in input().split(" ")]
lst2 = [int(s) for s in input().split(" ")]
s = 0
for i in lst1:
    for j in lst2:
        if i == j:
            s += 1
        break
print(s)
