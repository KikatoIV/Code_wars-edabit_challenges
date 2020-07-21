def is_in_order(txt):
    sort_txt = sorted(txt)
    empty_txt = ''
    for x in sort_txt:
        empty_txt += x
    if empty_txt == txt:
        return True
    else:
        return False

print(is_in_order("abc"))
