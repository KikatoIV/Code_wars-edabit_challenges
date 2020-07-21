def count(deck):
    count = 0
    bad = [10 , "J", "Q", "K", "A"]
    good = [2,3,4,5,6]
    for i in deck:
        if i in good:
            count += 1
        elif i in bad:
            count -= 1
        else:
            pass 
    return count

# a cool short way to code this

count=lambda d:sum(-1 if i in [10,'J','Q','K','A']else 1if i>1and i<7else 0for i in d)

print(count([2, 3, 4, 5, 'J', 'A', 4, 8, 5]))
print(count(['A', 'A', 'K', 'Q', 'Q', 'J']))