

def is_triangle(a,b,c):
    if (a + b > c) or (b + c > a) or (c + a > b):
        print("no")
    else:
        print("yes")

def is_triangle2(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")

def give_lenghts():
    a = int(input("give a: "))
    b = int(input("give b: "))
    c = int(input("give c: "))
    return is_triangle(a,b,c)
    #return is_triangle2(a,b,c)


give_lenghts()

