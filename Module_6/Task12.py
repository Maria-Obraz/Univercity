x = input()
h1 = x.index("h", 0, len(x))
h2 = x.rindex("h", h1 + 1, len(x))
x2 = x[:h1 + 1]
x3 = x[h2:]
xnew = x[h1+1:h2]
xnew1 = xnew.replace("h", "H")
print(x2, xnew1, x3, sep="")
