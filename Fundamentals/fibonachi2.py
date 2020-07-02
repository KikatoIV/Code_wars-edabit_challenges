def fibo():
    i = 1
    num = input("how much would you like to genererate: ")
    if num == 0:
        fib = [0]
    elif num == 1:
        fin = [1]
    elif num == 2:
        fib[1,1]
    elif num > 2:
        fib = [1,1]
        while i <(num - 1):
            fib.append(fib[i]+ fib[i-1])
            i += 1
        return fib

print(fibo())
