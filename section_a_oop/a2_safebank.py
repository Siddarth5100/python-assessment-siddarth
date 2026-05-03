class BankAccount:
    def __init__(self, acc_holder_name, initial_amount):
        if initial_amount < 500:
            raise ValueError("Minimum deposit amount: 500")
        
        self.acc_holder_name = acc_holder_name
        self.__balance = initial_amount
        print(f"Account Holder: {acc_holder_name}, Amount added: {initial_amount}")

        self.transactions = []

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount should not be negative or zero")
        else:
            self.__balance += amount
            return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount should not be negative or zero")

        if amount > self.__balance:
            raise ValueError(f"Insufficient balance: {self.__balance}, Entered amount: {amount}")
        
        self.__balance -= amount
        return self.__balance
    
    def print_statement(self):
        print(f"")

# try:
#     ba = BankAccount("Aruna", 50)
#     print(f"Balance Amount: {ba.get_balance()}")
# except ValueError as e:
#     print(e)

ba = BankAccount("Aruna", 500)
print(f"Total balance amount: {ba.get_balance()}")

print(f"Deposited Amount: {ba.deposit(100)}")

# try:
#     ba.withdraw(10000)
#     print(f"Withdraw Amount: {ba.get_balance()}")
# except ValueError as e:
#     print(e)