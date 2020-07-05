import math

def cone_volume(h, r):
    if(h and r == 0):
        return 0
    return round((math.pi*r**2*h)/3,2)