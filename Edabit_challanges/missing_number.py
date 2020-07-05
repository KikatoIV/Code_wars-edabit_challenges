def missing_num(lst):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans = set(a) - set(lst)
    ans = list(ans)
    return ans[0]


print(missing_num([1, 2, 3,  4, 6, 7, 8, 9, 10]))

def missing_num(lst):
    for i in range(1,11):
        if i not in lst:
            return i