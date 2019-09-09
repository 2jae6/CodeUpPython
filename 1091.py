a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

result = a

for i in range(1, n):
    result = result * m + d

print(result)

