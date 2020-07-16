def factorial(n):
    ac = 1
    for i in range(1, n+1):
        ac = ac*i

    return ac

def binomial(n, r):
    res = factorial(n) / (factorial(r)*factorial(n - r))
    return res

def bernoulli(n):
    if n == 0:
        return 1
    else:
        coef = -1 / (n + 1)
        ac = 0
        for k in range(0, n):
            ac = ac + binomial(n + 1, k) * bernoulli(k)
        return coef * ac
            