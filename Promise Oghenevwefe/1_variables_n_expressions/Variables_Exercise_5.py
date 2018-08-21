# A python program to compute the compound interest

principalAmount = 10000
numberOfTimes = 12
interestRate = 8/100

numberOfYears = int(input("Enter the number of years the money would be compounded for: "))

compoundInterest = principalAmount * (1 + (interestRate/numberOfTimes))**(numberOfTimes*numberOfYears)

print("The final amount is: " + str(round(compoundInterest,2)))
