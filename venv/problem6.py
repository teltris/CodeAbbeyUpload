import math

n = int(input())

for i in range(0,n):
    a_list = input().split()
    map_obj = map(int,a_list)
    int_liste = list(map_obj)

    temp = int_liste[0] / int_liste[1]

    if temp % 1 == 0.5:
        ans = temp + 0.5
    elif temp % 1 > 0.5:
        ans = math.ceil(temp)
    else:
        ans = math.floor(temp)

    print(str(int(ans))+ " " )

