class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        print("Недостаточно средств")

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"


myAccount = BankAccount('Demzez', 200000)
myAccount.deposit(100)
print(myAccount)

myAccount.withdraw(100)
print(myAccount)

myAccount.apply_interest()
print(myAccount)

BankAccount.set_interest_rate(0.2)
myAccount.apply_interest()
print(myAccount)

print(BankAccount.validate_amount(100))
print(myAccount.validate_amount(100))
