def society_name(friends):
    friends.sort()
    return ''.join(x[0] for x in friends)
    
print(society_name(["Adam", "Sarah", "Malcolm"]))