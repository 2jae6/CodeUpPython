r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
count = 0


for x in range(r):
    for y in range(g):
        for z in range(b):
            print("%d %d %d" %(x, y,  z))
            count = count + 1

print(count)
