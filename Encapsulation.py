class Bank():
    def __init__(self):
        self.balance=500

    def get_balance(self):
        return self.balance

    def deposite(self,amount):
        self.balance += amount

s=Bank()
s.deposite(1000)

print(s.get_balance())