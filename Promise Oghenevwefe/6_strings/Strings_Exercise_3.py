
def count_letters(myString, myLetter):
    count = 0
    for char in myString:
        if char == myLetter:
            count += 1
    return count

myString = "Banana"
myLetter = "n"
print("Total number of " + myLetter + " in " + myString + " is " +
      str(count_letters(myString, myLetter)))

    
