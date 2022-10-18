N = int(input())
h = (N // 60) % 24
m = N % 60
print(f'{h}:{m}')
