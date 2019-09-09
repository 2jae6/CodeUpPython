a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

result = a

for i in range(1, n):
    result = result * r

print(result)

