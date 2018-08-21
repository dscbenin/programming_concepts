# Write a function to count how many odd numbers are in a list

def count_odd_numbers(myList):
    totalOddNumbers = 0
    for x in myList:
        if(x%2) == 1:
            totalOddNumbers += 1
    return totalOddNumbers

myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Total odd Numbers: " + str(count_odd_numbers(myList))) 
            
