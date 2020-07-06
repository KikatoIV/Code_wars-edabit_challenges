def left_digit(num):
    new = []
    for i in num:
        new.append(i)
        for x in new:
            if x.isdigit():
                return int(x) 
                break
 
        

print(left_digit("TrAdE2W1n95!"))