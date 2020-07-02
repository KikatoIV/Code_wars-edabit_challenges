def binary_array_to_num(arr):
    i, inter = 0,0
    leng = len(arr)
    while i < leng:
        inter += int(arr[leng -1 - i])*pow(2,i)
        i+= 1
    return inter
    
#shorter solution is using join and mapping 

#print(binary_array_to_num([0, 0, 0, 1]))
arr = [0,1,0,1]
list_To_String = int(''.join(map(str,arr)),2)
print(list_To_String)
