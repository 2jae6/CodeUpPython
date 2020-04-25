n = int(input())
a = [[0] * 20 for c in range(20)]

for i in range(n):

        x, y = input().split()
        x = int(x)
        y = int(y)
        a[x][y] = 1
        
for i in  range(19):

    for j in range(19):
        print(a[j][i])
        
    print("\n")
