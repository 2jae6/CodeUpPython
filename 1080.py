a=int(input())
i = 1
for x in range(1001):
    i = i + x
    if i > a:
        print(x)
        break
