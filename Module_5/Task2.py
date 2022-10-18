x = int(input())
n = 0
while 2**(n+1) < x:
    n += 1
print(n, 2**n)
