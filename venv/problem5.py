n = int(input())

for i in range(0,n):
    a,b,c = input().split()
    if int(a) < int(b):
        if int(a) < int(c):
            d = a
        if int(c) < int(a):
            d = c

    else:
        if int(b) < int(c):
            d = b
        if int(c) < int(b):
            d = c

    print(d+ " ")