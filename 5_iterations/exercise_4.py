def word_len_counter(providedlist):
    word_counter=0
    for i in providedlist:
        if(len(i) == 5):
            word_counter+=1
        else:
            pass

    return word_counter

xs=["Peter", "Griffin", "Lois", "Meg", "Chris", "Stewie", "Brian", "Quagmire", "Giggitty"]
print("The number of words that have ONLY 5 characters in the provided list is ", word_len_counter(xs))
