# ==============================================================================
#* OOP - Challenge: BANK Account
# ==============================================================================

class BankAccount():
    
    def __init__(self, owner: str, balance: int = 0):
        
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"\nAccount owner:   {self.owner}\nBalance:         {self.balance}"
    
    def deposit(self, money: int):
        self.balance += abs(money)
        print(f"\n{money} has been deposited to {self.owner}'s account.\nBalance: {self.balance}")

    def withdraw(self, money):
        if (self.balance - money) < 0:
            print(f"\nWidraw cannot possible, balance is too low!")
        else:
            self.balance -= money
            print(f"\nWidraw completed.\nBalance: {self.balance}")
            
acct1 = BankAccount("Zsolt", 10000)
print(acct1)

acct1.deposit(9000)
acct1.withdraw(14000)
acct1.withdraw(9000)
print(acct1)