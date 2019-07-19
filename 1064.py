a, b, c= input().split()
a = int(a)
b = int(b)
c = int(c)

print("%d" %(a if ((a < b) & (a < c)) else (b if((b < a) & (b < c)) else c)))
