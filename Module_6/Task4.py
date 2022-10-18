lst = [int(s) for s in input().split(" ")]
maxi = lst[0]
mini = lst[0]
i = 0
while i < len(lst):
    if lst[i] < mini:
        mini = i
    if lst[i] > maxi:
        maxi = i
        i += 1
    t = lst[mini]
    lst[mini] = lst[maxi]
    lst[maxi] = t
    print(lst)
