class Account(object):
    '''
    My account class
    '''

    def __init__(self, accountName):
        '''
        Create a new account and initialize the name and the balance
        every neew account is initialized with 1000
        '''

        self.name = accountName
        self.balance = 1000.0

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def __str__(self):
        return "Account Name: {0}, Account Balance: {1}".format(self.name, self.balance)

    def deposit(self, amount):

        if amount < 0:
            print("invalid input")
        else:
            self.balance += amount

