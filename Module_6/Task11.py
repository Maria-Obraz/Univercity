x = input()
h1 = x.index("h", 0, len(x))
h2 = x.rindex("h", h1 + 1, len(x))
x_new = x[h1+1:h2]
xnew_rev = x_new[::-1]
x2 = x[:h1+1]
x3 = x[h2:]
print(x2, xnew_rev, x3, sep="")
