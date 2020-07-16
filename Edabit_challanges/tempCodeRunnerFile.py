def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(m,k):
    if k <= m:
        return factorial(m)/(factorial(k) * factorial(m - k))
    else:
        return 0

def bernoulli_number(m):
    if m == 0:
        return 1
    else:
        t = 0
        for k in range(0, m):
            t += combination(m, k) * bernoulli_number(k) / (m - k + 1)
        return 1 - t

print(bernoulli_number(2))