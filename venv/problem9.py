# if value 1 + value 2 is smaller than value 3, a triangle cannot be built
# value 1 , value 2 , value 3 can all be a b or c


n = int(input())

for i in range(0,n):
    a_list = input().split()
    map_obj = map(int, a_list)
    liste = list(map_obj)
    liste.sort()

    if liste[0] + liste[1] < liste[2]:
        ans = 0
    else:
        ans = 1

    print(str(ans)+ " ")

