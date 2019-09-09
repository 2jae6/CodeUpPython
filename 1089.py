a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

result = a

for i in range(1, n):
    result = result + d

print(result)

