from datetime import datetime

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
        self.transactions = []


    def deposit(self, amount):
        try:
            amount + 10
        except TypeError:
            return f"Please enter {amount} in figures"
        if amount <= 0:
            return f"Please deposit a valid amount"
        else:
            self.balance += amount
            transaction = {"amount": amount,"balance":self.balance,"narration":"You deposited", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
   
    def withdraw (self,amount):
        try:
            amount + 10
        except TypeError:
            return f"Please enter {amount} in figures"
        
        if amount <= 0:
            return "Input valid amount"
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            widthrawal = amount + self.transaction_fee #holds both the transaction fee and withdrawal amount
            self.balance -= widthrawal
            transaction = {"amount": amount,"balance":self.balance,"narration":"You withdrew", "time":datetime.now()}
            self.transactions.append(transaction)
           
            return f"Hello {self.name}, you have successfully withdrawn {amount}. Your current balance is {self.balance}"
    
    def borrow(self,amount):
        try:
            amount + 10
        except TypeError:
            return f"Please enter {amount} in figures"
        total_fees= self.loan_fees* amount / 100
        
        if amount <= 0:
            return "Please input a valid amount"
        elif self.loan_amount > 0:
            return "You have an outstanding loan balance"
        elif amount > self.loan_limit:
            return "You have exceded the limited borrowing amount"
        else:
            self.loan_amount +=total_fees + amount
            self.balance += amount
            transaction = {"amount": amount,"balance":self.balance,"narration":"You borrowed", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"Dear customer, you have received a loan amount of {amount} and your current balance is {self.balance}. Your total loan amount is {self.loan_amount}"
    
    def repay(self,amount):
        try:
            amount + 10
        except TypeError:
            return f"Please enter {amount} in figures"
        if amount < self.loan_amount:
            self.loan_amount -=amount
            transaction = {"amount": amount,"balance":self.balance,"narration":"You repayed", "time":datetime.now()}
            self.transactions.append(transaction)
            return f" You have repayed {amount} of your loan. Your current loan balance is {self.loan_amount}"
        elif amount > self.loan_amount:
            balance = amount - self.loan_amount
            self.balance +=balance
            self.loan_amount = 0
            transaction = {"amount": amount,"balance":self.balance,"narration":"You repayed", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"Congratulations! You have repayed your loan! Your current loan balance is {self.loan_amount} and your current balance is {self.balance}"
        elif amount == self.loan_amount:
            transaction = {"amount": amount,"balance":self.balance,"narration":"You repayed", "time":datetime.now()}
            self.transactions.append(transaction)
            return f" Congratulations!! You have fully your loan of {self.loan_amount}. Your current loan balance is {self.loan_amount-amount}"
        else:
              
              return f"Dear customer, you still have a loan balance of {self.loan_amount}"
    
    def transfer(self,amount,account):
        try:
            amount + 10
        except TypeError:
            return f"Please enter {amount} in figures"
        if amount <= 0:
            return f"Please transfer a valid amount"
        fee = amount * 0.05
        total = amount + fee
        if total > self.balance:
            return f"Your balance is {self.balance} you need {total} in order to transfer {amount}"
        else:
            self.balance -= total
            account.deposit(amount)
            transaction = {"amount": amount,"balance":self.balance,"narration":"You transfered", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"Dear customer, you have transfered {amount} to accout {account.name}. Your new account balance is {self.balance}"

    def get_statement(self):
        for transaction  in self.transactions:
            amount = transaction["amount"]
            narration = transaction["narration"]
            balance = transaction["balance"]
            time = transaction["time"]
            date = time.strftime("%D")
            print (f" {date} .... {narration} .... {amount} ....Balance {balance}")

class MobileMoneyAccount(Account):
    def __init__(self, name, phone, service_provider):
        Account.__init__(self,name, phone)
        self.service_provider = service_provider

    def buy_airtime(self,amount):
        try:
            amount + 10
        except TypeError:
            return f"Please enter {amount} in figures"
        if amount <= 0:
            return f"Please enter a valid amount"
        elif amount <= self.balance:
            self.balance-=amount
            transaction = {"amount": amount,"balance":self.balance,"narration":"You bought Airtime", "time":datetime.now()}
            self.transactions.append(transaction)
            return f"You have bought {amount} airtime. Your current {self.service_provider} mobile money balance is {self.balance}"
          








