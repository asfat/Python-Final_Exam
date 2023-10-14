import random
from abc import ABC,abstractmethod

class Bank(ABC):
    accounts=[]
    bank_balance=0
    loan_Feature=True
    total_loan=0
    def __init__(self) -> None:
        pass

class User(Bank):

    def __init__(self,name,email,address,account_type) -> None:
        super().__init__()
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.__balance=0
        self.__loan=1
        self.accountId=random.randint(5000,10000)
        Bank.accounts.append(self)

    def account_id(self):
        print(f'Note your account Id: {self.accountId}\n')

    def deposite(self,ammount):
        if ammount>=0:
            self.__balance+=ammount
            Bank.bank_balance+=ammount
    
    def withdraw(self,ammount):
        if ammount>=0 and ammount<=self.__balance:
            if ammount>Bank.bank_balance:
                print(' bank is bankrupt')
            else:
                self.__balance-=ammount
                Bank.bank_balance-=ammount
                print(f'your withdrawl money: {ammount} and balance after withdrawl: {self.__balance}')

    def check_balance(self):
        print(f'Your current balance is: {self.__balance}')

    def take_loan(self,ammount):
        if Bank.loan_Feature==True:

            if self.__loan==1:
                self.__loan+=1
                self.__balance+=ammount
                Bank.total_loan+=ammount
                print(f'\nYou got the loan: {ammount}. Your balance after loan: {self.__balance}')
            elif self.__loan==2:
                self.__loan+=1
                self.__balance+=ammount
                Bank.total_loan+=ammount
                print(f'\nYou got the loan: {ammount}. Your balance after loan: {self.__balance}')
            else:
                print('\nYou cannot take loan more than 2 times.\n')


    def transection_history(self):
        print(f'Your current Balance is:{self.__balance}')

        if self.__loan==1:
            print('You are allowed to take loans 2 times.')
        elif self.__loan==2:
            print('You are allowed to take loan 1 time.')
        else:
            print('You can\'t take loans. Please pay your previous loans ')

    flag=False
    def pay_another_account(self,accountNo,ammount):

        if self.__balance>=ammount:

            for account in Bank.accounts:
                if account.accountId==accountNo:
                    flag=True
                    print('\nAccount Id is found. Payment processing\n')
                    self.__balance-=ammount
                    account.__balance+=ammount
                    print(f'{ammount} is send. Your current balance is {self.__balance}')
            
            if flag==False:
                print('Account does not exist')

        else:
            print(f'Your current balance is: {self.__balance}. Please deposite on your account.')

class Admin(Bank):
    def __init__(self,name, email, address, account_type) -> None:
        super().__init__()
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.accountId=random.randint(5000,10000)
        Bank.accounts.append(self)

    def account_id(self):
        print(f'Note your account Id: {self.accountId}\n')
    
    def create_account(self,name,email,address,account_type):
        user=User(name,email,address,account_type)

    def delete_account(self,account_No):
        for account in Bank.accounts:
            if account.accountId==account_No:
                print(f'\nYou are removing {account}\n')
                Bank.accounts.remove(account)
                print('\nSuccesfully Removed.!\n')

    def all_users(self):
        for account in Bank.accounts:
            for list in account:
                print(f'{list.name}, email {list.email}, Account Type:{list.account_type}, Account Id {list.accountId} and balance:{list.__balance}\n')
    
    def bank_balance(self):
        print(f'Current bank balance is: {Bank.bank_balance}')
        
    def bank_loan(self):
        print(f'Current bank balance is: {Bank.total_loan}')

    def TurnOff_Loan(self):
        Bank.loan_Feature=False
    
    def TurnOn_Loan(self):
        Bank.loan_Feature=True

currentUser=None
while True:
    if currentUser==None:
        print('\nNo Logged User Found!\n')
        ch=input('\nLogin Or Register: (L/R)')
        if ch=='R':
            print('\nFor register an account we need below information.\n')
            name=input('Enter your name: ')
            email=input('Enter your Email: ')
            address=input('Enter your address: ')
            account_type=input('Savings, Cuurent and Admin (sav/cur/admin)')

            if account_type=='sav':
                user=User(name,email,address,account_type)
                currentUser=user
                print('\nNote down your account Id For next time Login\n')
                currentUser.account_id()
            elif account_type=='cur':
                user=User(name,email,address,account_type)
                currentUser=user
                print('\nNote down your account Id For next time Login\n')
                currentUser.account_id()
            elif account_type=='admin':
                admin=Admin(name,email,address,account_type)
                currentUser=admin
                print('\nNote down your account Id For next time Login\n')
                currentUser.account_id()
            else:
                print('Invalid input')

        if ch=='L':
            print('Give your email address and account Id')
            email=input('Email: ')
            account_id=int(input('Account Id:'))

            for account in Bank.accounts:
                if account.email==email and account.accountId==account_id:
                    currentUser=account
                    print(f'\n welcome {currentUser.name}!\n')
    
    else:
        if currentUser.account_type=='sav' or currentUser.account_type=='cur':
            print('Option 1: Deposite\n')
            print('Option 2: withdraw\n')
            print('Option 3: check Balance\n')
            print('Option 4: Take Loan\n')
            print('Option 5: Transection History\n')
            print('Option 6: Pay Another Account\n')
            print('Option 7: Log Out\n')

            op=int(input('Choose Option (1/2/3/4/5/6/7): '))

            if op==1:
                ammount=int(input('Enter Ammount: '))
                currentUser.deposite(ammount)
            elif op==2:
                ammount=int(input('Enter Ammount: '))
                currentUser.withdraw(ammount)
            elif op==3:
                currentUser.check_balance()
            elif op==4:
                ammount=int(input('Enter Ammount: '))
                currentUser.take_loan(ammount)
            elif op==5:
                currentUser.transection_history()
            elif op==6:
                account_id=int(input('Account Id:'))
                ammount=int(input('Enter Ammount: '))
                currentUser.pay_another_account(ammount,account_id)

            elif op==7:
                currentUser=None
            else:
                print('Invalid Input. Please check and give correct Info')
        
        elif currentUser.account_type=='admin':
            print('Option 1: create_account\n')
            print('Option 2: delete_account\n')
            print('Option 3: all users info\n')
            print('Option 4: Show Total bank balance\n')
            print('Option 5: Show Total bank loan\n')
            print('Option 6: Turn On Loan Features\n')
            print('Option 7: Turn Off Loan Features\n')
            print('Option 8: Log Out\n')

            op=int(input('Choose Option (1/2/3/....): '))

            if op==1:
                name=input('Enter  name: ')
                email=input('Enter  Email: ')
                address=input('Enter  address: ')
                account_type=input('Savings, Cuurent and Admin (sav/cur/admin)')
                if account_type=='sav' or account_type=='cur':
                    user=User(name,email,address,account_type)
                    user.account_id()
                elif account_type=='admin':
                    admin=Admin(name,email,address,account_type)
                    admin.account_id()
            elif op==2:
                
                account_no=int(input('--\nEnter Account No:'))
                currentUser.delete_account(account_no)
            
            elif op==3:
                currentUser.all_users()
            elif op==4:
                currentUser.bank_balance()
            
            elif op==5:
                currentUser.bank_loan()

            elif op==6:
                currentUser.TurnOn_Loan()
            
            elif op==7:
                currentUser.TurnOff_Loan()
            
            elif op==8:
                currentUser=None
            else:
                print('Invalid info. Please give correct Information.\n')

    


    