def check_display_balance(account, expected_balance):
 import io
 import sys
 captured_output = io.StringIO()
 sys_stdout = sys.stdout
 sys.stdout = captured_output
 try:
  account.display_balance()
 finally:
  sys.stdout = sys_stdout
 output = captured_output.getvalue().strip()
 expected_output = f"Current Balance: ${expected_balance}"
 return output == expected_output
# BankAccount class encapsulating basic banking operations
class BankAccount:
 def __init__(self, initial_balance=0):
  self.__account_balance = initial_balance

 def deposit(self, amount):
  if amount > 0:
   self.__account_balance += amount

 def withdraw(self, amount):
  if 0 < amount <= self.__account_balance:
   self.__account_balance -= amount
   return True
  return False

 def display_balance(self):
  print(f"Current Balance: ${self.__account_balance}")