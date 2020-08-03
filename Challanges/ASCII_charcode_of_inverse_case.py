def counterpartCharCode(char):
    if str(char).isupper():
        return ord(str(char.lower()))
    if str(char).islower():
        return ord(str(char.upper()))
    else:
        return ord(char)
print(counterpartCharCode('L'))
