def maximum_score(tile_hand):
    total = 0
    for i in tile_hand:
        total += i["score"]
    return total
