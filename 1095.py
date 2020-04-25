n = int(input())
b = list(map(int, input().split()))
min = [99999]
arr = []

for i in range(n):
    arr.append(b[i])
    if min[0] > arr[i]:
        min[0] = arr[i]

print(min[0])
