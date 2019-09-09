w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)



print("%.2f MB" %((((w * h * b)/8)/1024)/1024))


