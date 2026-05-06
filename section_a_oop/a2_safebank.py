class BankAccount:
    def __init__(self, acc_holder_name, initial_amount):
        if initial_amount < 500:
            raise ValueError("Minimum deposit amount: 500")
        
        self.acc_holder_name = acc_holder_name
        self.__balance = initial_amount
        print(f"Account Holder: {acc_holder_name}, Amount added: {initial_amount}")
        
        self.transaction_details = []
        self.transaction_details.append(f"Account created, Account Holder: {acc_holder_name}, Initial deposit amount: {initial_amount}")

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount should not be negative or zero")
        else:
            self.__balance += amount
            self.transaction_details.append(f"Amount Deposited: {amount}, Balance Amount: {self.__balance}")
            return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount should not be negative or zero")

        if amount > self.__balance:
            raise ValueError(f"Insufficient balance: {self.__balance}, Entered amount: {amount}")
        
        self.__balance -= amount
        self.transaction_details.append(f"Amount Withdraw: {amount}, Balance Amount: {self.__balance}")
        return self.__balance
    
    def print_statement(self):
        print(f"")

# try:
#     ba = BankAccount("Aruna", 50)
#     print(f"Balance Amount: {ba.get_balance()}")
# except ValueError as e:
#     print(e)

ba = BankAccount("Aruna", 500)
# print(f"Total balance amount: {ba.get_balance()}")

# print(f"Deposited Amount: {ba.deposit(100)}")

# try:
#     ba.withdraw(10000)
#     print(f"Withdraw Amount: {ba.get_balance()}")
# except ValueError as e:
#     print(e)

# print(ba.acc_holder_name)
# ba.acc_holder_name = "siddarth"
# print(ba.acc_holder_name)

# print(ba.__balance)
# print(ba.get_balance())
# ba.__balance = 100
# print(ba.get_balance())
# ba.deposit(2500)
# print(ba.get_balance())
# print(ba.transaction_details)
# ba.deposit(2500)
# print(ba.transaction_details)
# ba.withdraw(100)
# print(ba.transaction_details)

# ba = BankAccount("Bala", 100)

# print(ba.transaction_details)
# ba.deposit(2500)
# print(ba.transaction_details)

# acc = BankAccount("Arun Kumar", 1000)
# print(acc.transaction_details)

# acc.deposit(500)
# print(acc.transaction_details)

# acc.withdraw(300)
# print(acc.transaction_details)

# acc.withdraw(5000)
# print(acc.transaction_details)
