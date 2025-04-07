class BankAccount:
    def __init__(self,initial_balance,owner):
        self.initial_balance = initial_balance#protected
        self.owner = owner#public
        self._pin = "1234"#private
    def deposit(self,amount):
        if amount > 0:
            self.balance =amount
            print(f"deposited :{amount}")
            return True
        else:
            print("amount must be positive")
            return False
    def withdrawal(self,amount):
        if amount < self.balance:
            self.balance = amount
            print(f"withdrawn: {amount} ")
            return True
        else:
            print("amount must be positive")
            return False
    def get_balance(self):
        return self.balance
    def verify_pin(self,attempted_pin):
         return self ._pin == attempted_pin
    def change_pin(self,new_pin):
        return self._pin == new_pin
        
account = BankAccount(1000,"Dorothy")
# print(account.owner)
# account.balance = 2000
# print(account.balance)
print(account._pin("1234"))
    


        