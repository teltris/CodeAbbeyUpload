

def haupt():
    n = int(input())

    for i in range(n):
        a_List = input().split()
        map_obj = map(int, a_List)
        liste = list(map_obj)
        calculation = liste[0]*liste[1] + liste[2]
        ans = split_up(calculation)
        print(str(ans) + " ")


def split_up(calc):
    sum = [int(i) for i in str(calc)]
    ans = 0
    for k in range(len(sum)):
        ans += sum[k]
    return ans

haupt()
