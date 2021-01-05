import math

a_list = input().split()
map_obj = map(int, a_list)
liste = list(map_obj)



for i in range(0,liste[0]):
    fahrenheit = liste[i+1]
    celsius = (fahrenheit - 32) / 1.8

    if celsius % 1 == 0.5:
        ans = celsius +0.5
    if celsius % 1 > 0.5:
        ans = math.ceil(celsius)
    else:
        ans = math.floor(celsius)

    print(str(ans) + " ")

