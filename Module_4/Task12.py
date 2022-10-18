year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
m = int(input())
d = int(input())
if (year[m] > d):
    print(f'{d+1}-{m}-2022')
else:
    print(f'1-{m+1}-2022')
