n = int(input())
b = list(map(int, input().split()))
arr = [0 for i in range(24)]



for i in range(n):
    arr[b[i]] = arr[b[i]] + 1
    
for i in range(1, 24):
    print(arr[i], end = ' ')
