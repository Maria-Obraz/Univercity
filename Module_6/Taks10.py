x = input()
h1 = x.index("h", 0, len(x))
h2 = x.rindex("h", h1+1, len(x))
x2 = x[:h1]
x3 = x[h2+1:]
print(x2, x3, sep="")
