def alphanumeric_restriction(s):
    if s.isalpha():
        return True
    elif s.isdigit():
        return True
    else:
        return False

print(alphanumeric_restriction("Bo2ld"))

