def find_bob(names):
    elem = "Bob"
    try:
        index_pos = names.index(elem)
        return index_pos

    except:
        return -1





print(find_bob(["Jimmy", "Layla", "Bob"]))