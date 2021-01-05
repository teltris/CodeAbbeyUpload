anzahl = int(input())

for i in range(0,anzahl):
    a_list = input().split()
    map_obj = map(int,a_list)
    liste = list(map_obj)

    a = liste[0]
    b = liste[1]
    n = liste[2]

    ans = 0


    for repeats in range(0,n):
        ans += a + b * repeats


    print(str(ans)+" ")