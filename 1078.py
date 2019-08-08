a = input()
a = int(a)
b = 0
result = 0
while a != b:
    b = b + 1
    if b % 2 == 0:
        result = result + b
    if a == b:
        print(result)
        break

