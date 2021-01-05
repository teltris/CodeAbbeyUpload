n = int(input())

for i in range(0,n):
    a,b = input().split()
    if int(b) > int(a):
        d = a
    else:
        d = b

    print(d+ " ")