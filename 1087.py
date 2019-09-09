w = input()
w = int(w)
result = 0

for i in range(1, w + 1):
    result = result + i
    if result >= w:
        print(result)
        break


