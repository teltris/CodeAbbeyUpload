
def find_steigung(a,b,c,d):
    return (d - b) / (c - a)

def find_b(a,b,m):
    return (b - m * a)

def linear_function():
    answer = []
    n = int(input())
    for i in range(n):
        a, b, c, d = [int(x) for x in input().split()]
        m = int(find_steigung(a,b,c,d))  #Formeln für Steigung
        b_formula = int(find_b(a,b,m)) #Einfach GS umgestellt
        print("({0} {1})".format(m, b_formula) + " ")

linear_function()


