class Account():
    pass

    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
        
    def deposit(self, amount):
        self.balance+=amount
        return "Deposit has been accepted"

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            return "Withdraw has been accepted"
        return "Insufficient funds"

name=str(input())
capital=int(input())
capital2=int(input())
result=Account(name, capital)
print(result.deposit(capital2))