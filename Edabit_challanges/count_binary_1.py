def count_ones(num):
    num = bin(num)
    return str(num[2:]).count("1")

print(count_ones(12))
