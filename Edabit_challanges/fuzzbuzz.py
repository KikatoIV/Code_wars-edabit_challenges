def fizz_buzz(num):
    a = ''
    if num%3 == 0:
        a = a + "Fizz"
    if num%5 == 0:
        a = a + "Buzz"
    if num%3 != 0 and num%5 != 0:
        return str(num)
    return a

print(fizz_buzz(''))