class Account:
    account_type = "student"
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.balance = 0
        self.transaction_fee = 50
        self.loan_amount = 0
        self.loan_fees = 5
        self.loan_limit = 50000


    def deposit(self, amount):
        if amount <= 0:
            return f"Please deposit a valid amount"
        else:
            self.balance += amount
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
   
    def withdraw (self,amount):
        
        if amount <= 0:
            return "Input valid amount"
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            widthrawal = amount + self.transaction_fee #holds both the transaction fee and withdrawal amount
            self.balance -= widthrawal
            
           
            return f"Hello {self.name}, you have successfully withdrawn {amount}. Your current balance is {self.balance}"
    
    def borrow(self,borrowed_amount):
        total_fees= self.loan_fees* borrowed_amount / 100
        
        if borrowed_amount <= 0:
            return "Please input a valid amount"
        elif self.loan_amount > 0:
            return "You have an outstanding loan balance"
        elif borrowed_amount > self.loan_limit:
            return "You have exceded the limited borrowing amount"
        else:
            self.loan_amount +=total_fees + borrowed_amount
            self.balance += borrowed_amount
            return f"Dear customer, you have received a loan amount of {borrowed_amount} and your current balance is {self.balance}. Your total loan amount is {self.loan_amount}"










