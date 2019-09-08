a = input()
a = int(a)
result = []
for i in range(a + 1):
    if (i % 3) == 0:
        result.append('X')
    else: result.append(str(i))

for i in range (1, a + 1):
    print(result[i], end = ' ')
