def int_to_str(num):
    num = str(num)
    ''.join(list(num))
    return type(num)

def str_to_int(num):
    num = int(num)+ 0
    return type(num)

print(str_to_int('4'))
print(str_to_int('65'))