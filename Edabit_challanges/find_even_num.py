def find_even_nums(num):
    take_away = 0
    if num == 1:
        return []
    if num%2 != 0:
        take_away += num%2
    if num%2 == 0:
        num += 2
    return [x for x in range(num + take_away) if x%2 == 0 and x != 0]


print(find_even_nums(13))