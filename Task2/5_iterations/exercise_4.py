def len5word(stuff):
    count = 0
    for word in stuff:
        if len(word) == 5:
            count +=1
    return count
