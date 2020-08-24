#Author: Himanshu Sharma
#Creating dictionary of accounts
A1 = {
  "name" : "Amar",
  "Address" : "New Delhi",
  "AccountType" : "Saving",
  "Balance" : 60000
}
A2 = {
  "name" : "Akbar",
  "Address" : "Bengaluru",
  "AccountType" : "Saving",
  "Balance" : 200
}
A3 = {
  "name" : "Anthony",
  "Address" : "Hyderabad",
  "AccountType" : "Current",
  "Balance" : 20000
}

bankaccountlist = {
  "100001" : A1,
  "100002" : A2,
  "100003" : A3
}

class BankAccounts:
    no_of_accounts = len(bankaccountlist)

    def __init__(self):
        self.balance = 0
        self.accountno = 0
        self.type = ''
        
        
    def depositAmount(self, account,  amount):
        print('Depositing Amount: ', amount, 'to bank account', account)
        total_amount = float(amount)
        bankaccountlist[account]['Balance'] += total_amount
        print("\n Available balance is Rs.", bankaccountlist[account]['Balance']) 
        print('Your account', account, 'has been credited with Rs.' , total_amount)
        print('Your current balance is', bankaccountlist[account]['Balance'])
        print('Details:', bankaccountlist[account])

    def withdrawAmount(self, account, amount):
        if amount <= bankaccountlist[account]['Balance']:
            bankaccountlist[account]['Balance'] -=amount
        print('Withdrawing Amount:', amount, 'from bank account', account)
        print('Withdrawn Successfully')
        print('Your current balance is', bankaccountlist[account]['Balance'])
        print('Details:', bankaccountlist[account])

    def settingAccount(self):
        acc = input("Enter account number: ")
        name =input("Enter account holder name: ")
        add = input("Enter account holder address: ")
        typeacc =input("Enter account type (Saving/Current): ")
        bankaccountlist[acc] = {'name': name, 'Address': add, 'AccountType': typeacc, 'Balance': 0}
        print('Account Created with account number', acc, 'and details', bankaccountlist[acc])
    
    def gettingAccount(self, accountno):
        print('Getting Account Details for account number:',accountno, '\n')
        print('Details:', bankaccountlist[accountno])

def main():
    acc1 = BankAccounts()
    acc1.settingAccount()
    acc1.gettingAccount('100003')
    acc1.depositAmount('100003', 5000)
    acc1.withdrawAmount('100003', 200)

if __name__ == "__main__":
    main()