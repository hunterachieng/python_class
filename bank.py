class Account:
    account_type = "student"
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
    
    def borrow (self):
        return f"People with a {self.account_type} are now allowed to get a loan"

    def terminate (self):
        return f"The user with account number {self.account_number} is no longer a member of our bank"
    
    def registration (self):
        return f" Dear {self.account_name}, your new {self.account_type} account of number {self.account_number} has been activated"
    