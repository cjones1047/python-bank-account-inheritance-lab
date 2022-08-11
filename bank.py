from ast import BitAnd


class BankAccount():
  def __init__(self, balance=0, interest_rate=0.02):
    self.balance = balance
    self.interest_rate = interest_rate
    print("Thanks for creating an account!")
  def deposit(self, amount):
    if(amount < 0):
      return False
    self.balance += amount
    print(f"Recent deposit: ${amount}\nNew balance: ${self.balance}")
    return self.balance
  def withdraw(self, amount, overdraft_penalty=0):
    if(amount > self.balance and overdraft_penalty == 0):
      print(f"Sorry, you can't withdraw ${amount} if your account only has ${self.balance} in it...")
      return False
    if(amount > self.balance and overdraft_penalty > 0):
      print(f"You only have ${self.balance} in your account. Your request to withdraw ${amount} is ignored, and we have charged you an Overdraft Fee of ${overdraft_penalty}")
      self.balance -= overdraft_penalty
      return False
    self.balance -= amount
    print(f"Recent withdrawal: ${amount}\nNew balance: ${self.balance}")
    return self.balance
  def accumulate_interest(self, child=False, overdraft_penalty=0):
    if(overdraft_penalty > 0 and self.balance < 0):
      print(f"Your Overdraft Account doesn't accumulate interest since your balance is negative (Account Balance: {self.balance})")
      return False
    if(child == True):
      print(f"Your children's account just tacked on $10 in interest!")
      self.balance = self.balance + 10
      return self.balance
    else:
      print(f"Your account just accumulated ${self.balance * self.interest_rate} in interest!")
      self.balance = self.balance + (self.balance * self.interest_rate)
      return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
  def accumulate_interest(self, child=True):
    return super().accumulate_interest(child)
  
class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
  def withdraw(self, amount, overdraft_penalty=40):
    return super().withdraw(amount, overdraft_penalty)
  def accumulate_interest(self, child=False, overdraft_penalty=40):
    return super().accumulate_interest(child, overdraft_penalty)

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
