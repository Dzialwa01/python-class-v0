# Dzialwa Nemakonde
# 18 February 2026

class CreditCard:

    def __init__(self, name, number, bank="ABC Bank"): # bank is initialised if not given
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0


    def change(self, amount):
        if not(isinstance(amount, (int, float))) or (amount <=0): # ensuring that the amount is a number and it is not negative
            print("Change denied")
        else:
            self.balance += amount

    def pay(self, amount):
        if not(isinstance(amount, (int, float))) or (amount <=0) or (amount > self.balance): # Ensuring that the amount specified is a number and is also not exceeding the balance
            print("Change denied")
        else:
            self.balance -= amount

    def __str__(self): # This is what is printed when we just print the object
        info = f"Name: {self.name} \n Number: {self.number} \n Bank: {self.bank} \n Balance: {self.balance}"
        return info

u1 = CreditCard("Robert Welker", 123456789, "Standard Bank")
print(u1)

u1.change(2000)
print(u1)

u1.pay(500)
print(u1)