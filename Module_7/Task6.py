n1 = int(input())
dict1 = {}
for i in range(n1):
    lst = [str(s) for s in input().split(" ")]
    dict1[lst[0]] = list(lst[1:])
n2 = int(input())
ans = []
for i in range(n2):
    city = input()
    for k, v in dict1.items():
        if dict1[k].count(city) != 0:
            ans.append(k)
print(ans)

