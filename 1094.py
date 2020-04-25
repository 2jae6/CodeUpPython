n = int(input())
b = list(map(int, input().split()))
    
b.reverse()

for i in range(n):
    print(b[i], end = ' ')
