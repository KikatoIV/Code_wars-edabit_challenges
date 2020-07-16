def min_turns(current, target):
    current_lst = list(current)
    target_lst = list(target)
    x = 0
    rotate = 0
    while(current != target):
        if x == len(current_lst):
            return rotate
        if current_lst[x] != target_lst[x]:
            rotate += min(abs(int(current_lst[x]) - int(target_lst[x])), 10 - abs(int(current_lst[x]) - int(target_lst[x])))
        x += 1

print(min_turns('0000', '9999'))