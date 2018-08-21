# A program to count how many words in a list have length 5

def number_of_words(myList):
    totalNumberOfWords = 0
    for x in myList:
        if len(x) == 5:
            totalNumberOfWords += 1
    return totalNumberOfWords

myList = ['Hello','World','Come','Here','Coagh','Black','John']
print("The total number of words with length 5 is " + str(number_of_words(myList)))
