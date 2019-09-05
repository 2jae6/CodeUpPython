a = input()

for i in range(1, 16):
    result = '{0:x}'.format(int(a, 16) * i)
    print(a + '*' + '{0:x}'.format(i).upper() + '=' + result.upper())
