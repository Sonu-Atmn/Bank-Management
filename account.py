from bankinfo import bank
import shelve
import datetime



class Account:
   
    
    def __init__(self,name,mob) -> None:
        self.name=name
        self.mob=mob
        with shelve.open(r'bankdata\AccountFile') as actfile:
            length=len(actfile)
            
        self.account_number=bank.bank_accode+str(length+1)
        self.passbook=[]
        self.bank_balance=0
        self.DOB=""
        self.sex=""
        self.address=""
    
    def basic_info(self):
        print("Name: ",self.name)
        print("Mobile: ",self.mob)
        print("Account Number: ",self.account_number)
        print("Current Balance: ",self.bank_balance)
        
    def full_info(self):
        print("Name: ",self.name)
        print("Mobile: ",self.mob)
        print("Account Number: ",self.account_number)
        print("Date of Birth: ",self.DOB)
        print("Sex: ",self.sex)
        print("Address: ",self.address)
            
    def account_info(self,dob,sex,address):
        self.DOB=dob
        self.sex=sex
        self.address=address

    def credit(self,amnt):
        self.bank_balance+=amnt
        self.passbook.append(['+'+str(amnt),str(datetime.datetime.now()),self.bank_balance])
    
    def debit(self,amnt):
        if self.bank_balance<amnt:
            print("INSUFFICIENT BALANCE!!!!") 
        else:
            self.bank_balance-=amnt
            self.passbook.append(['-'+str(amnt),str(datetime.datetime.now()),self.bank_balance])
    
    def current_balance(self):
        print(f"Your current balance is: {self.bank_balance}")
        
    def __repr__(self) -> str:
         return 