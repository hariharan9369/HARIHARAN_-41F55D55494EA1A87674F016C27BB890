
class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          return f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}"
      else:
          return "Invalid deposit amount."

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__account_balance:
          self.__account_balance -= amount
          return f"Withdrew ₹{amount}. New balance: ${self.__account_balance}"
      elif amount > self.__account_balance:
          return "Insufficient funds."
      else:
          return "Invalid withdrawal amount."

  def display_balance(self):
      return f"Account Balance for {self.__account_holder_name}: ₹{self.__account_balance}"
if __name__ == "__main__":
  account = BankAccount("212203363", "hari", 90000.0)
  print(account.display_balance())
  print(account.deposit(800.0))
  print(account.withdraw(200.0))
  print(account.withdraw(15000.0))
  print(account.display_balance())