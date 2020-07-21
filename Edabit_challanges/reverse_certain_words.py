def reverse_string(strung, letter):
    new_lst = strung.split()
    new_str = ''
    for x in new_lst:
        if x.startswith(letter):
            new_str += " "  + x[::-1]
        else:
            new_str += " "+ x
    return new_str[1:]


print(reverse_string("Hey im here to test", "t"))