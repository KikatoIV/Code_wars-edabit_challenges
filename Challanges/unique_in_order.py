def unique_in_order(iterable):
    lst = []
    stng = ''
    for c in iterable:
        if c is stng:
            continue
        else:
            lst.append(c)
        stng = c
    return lst
print(unique_in_order('AAAABBBCCDAABBB'))


#this was a very clever solution i found
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

