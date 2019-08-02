a = input()
a = ord(a)
b = 97
while a != b:
    print("%s" %chr(b))
    b += 1
    if a == b:
        print("%s" %chr(b))
