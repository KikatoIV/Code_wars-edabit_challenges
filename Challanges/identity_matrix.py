import numpy as np

def id_mtrx(n):
    array_2D = []
    try:
        for i in range(n):
            for j in range(n):
                if i == j:
                    array_2D = 1
                else:
                    array_2D = 0
        array_2D = np.identity(n)
        return array_2D
    except:
        return "Error"

print(id_mtrx(2))

'''
def id_mtrx(n):
    	try:
		n, rev = abs(n), -1 if n<0 else 1
		return [[int(i=tha=j) for j in range(n)][::rev] for i in range(n)]
	except: return "Error"
'''