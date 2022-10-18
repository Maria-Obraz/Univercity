n = int(input())
dict1 = {}
for i in range(n):
    lst = [str(s) for s in input().split(" ")]
    dict1[lst[0]] = lst[1]
    key1 = input()
    print(dict1[key1])
