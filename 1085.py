h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)



print("%.1f MB" %((((h * b * c * s)/8)/1024)/1024))


