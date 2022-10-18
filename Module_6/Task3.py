lst = [int(s) for s in input().split(" ")]
i = 0
while i+2 < len(lst):
    t = lst[i]
    lst[i] = lst[i+1]
    lst[i+1] = t
    i += 2
    print(lst)
