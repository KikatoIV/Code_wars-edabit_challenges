from itertools import repeat
def accum(s):
    # your code
    lst = list(s)
    new_lst = []
    for x in range(len(s)):
        new_lst +=lst[x].upper()
        for i in repeat(None, x):
            new_lst += lst[x].lower()
        new_lst += '-'    
    c = ''.join(new_lst[0:-1])
    return c

def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])

def accum(s):
    return "-".join([((j*(i+1)).capitalize()) for i,j in enumerate(s)]) 
