# Question 3

import random
 
class Account:
    # Construct an Account object
    def _init_(self, AccountNum, name, balance = 0):
        self.AccountNum = AccountNum
        self.name = name
        self.balance = balance
 
    def getAccountNum(self):
        return self.AccountNum
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
 
    def main():
        accounts = []
        for i in range(1000,999999):
            account = Account(i, 0)
            accounts.append(account)
		
 
    while True:
 
       # Reading AccountNum from user
        AccountNum = int(input("\nEnter account Number: "))
 
        # Loop till AccountNum is valAccountNum
        while AccountNum < 1000 or AccountNum > 999999:
           AccountNum = int(input("\nInvalAccountNum AccountNum.. Re-enter: "))
 
        # Iterating over account session
        while True:
 
           # Printing menu
           print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - AcctNo_Details \t 5 - Exit ")
 
           # Reading selection
           selection = int(input("\nEnter your selection: "))
 
           # Getting account object
           for acc in accounts:
               # Comparing account AccountNum
               if acc.getAccountNum() == AccountNum:
                   accountObj = acc
                   break
 
           # View Balance
           if selection == 1:
               # Printing balance
               print(accountObj.getBalance())
 
           # Withdraw
           elif selection == 2:
               # Reading amount
               amt = float(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
 
               if ver_withdraw == "Yes":
                   print("Verify withdraw")
               else:
                   break
 
               if amt < accountObj.getBalance():
                  # Calling withdraw method
                  accountObj.withdraw(amt)
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
                    print("\nPlease make a deposit.");
 
           # Deposit
           elif selection == 3:
               # Reading amount
               amt = float(input("\nEnter amount to deposit: "))
               ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
 
               if ver_deposit == "Yes":
                  # Calling deposit method
                  accountObj.deposit(amt);
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
               else:
                   break
 
           elif selection == 4:
               print("nAccount Details")
               print("Account Number: ", self.AccountNum)
               print("Account holder Name ", self.name)
               print("Thanks for choosing us as your bank")
               exit()
           elif selection == 5:
               print("Thanks for choosing us as your bank")
               exit()
           # Any other choice
           else:
               print("nThat's an invalAccountNum choice.")
 
# Main function
main()
    
