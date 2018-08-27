def wordlength(myWords):
    words = 0
    for i in myWords:
        if len(i) == 5:
            words += 1
    return words

myWords = ["hello", "hi", "josh", "jacob", "moses", "debbie", "david"]
print("total number of words with five letters =", str(wordlength(myWords)))
