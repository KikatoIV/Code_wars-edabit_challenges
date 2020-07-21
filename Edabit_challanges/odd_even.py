def oddeven(lst):
    return len([x for x in lst if x%2]) > len([x for x in lst if not x%2])