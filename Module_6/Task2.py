lst = [int(s) for s in input().split(" ")]
i = 1
while i < len(lst):
    if lst[i] > lst[i-1]:
        print(lst[i], end=" ")
    i += 1
