n1 = int(input())
dict1 = {}
for i in range(n1):
    lst = [str(s) for s in input().split(" ")]
    for j in lst:
        try:
            dict1[j] = dict1[j] + 1
        except:
            dict1[j] = 1
print(sorted(dict1.values(), reverse=True))

