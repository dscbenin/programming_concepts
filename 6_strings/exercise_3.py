def count_letters(word, letter):
    char_counter=0
    for character in word:
        if character.lower() == letter.lower():
            #print("found")
            char_counter+=1
        else:
            pass
    return char_counter

word="DSC Benin is DSC Benin"
letter="D"
print(count_letters(word, letter))
