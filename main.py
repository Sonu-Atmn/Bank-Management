from typing import Any
import time
import os
import shelve
from bankinfo import bank
from account import Account
import TranactionPdfConvertor
import loginpage
from emailsender import send_email



cwd = os.getcwd()

folder_name = "bankdata"
scfoldername="pdfs"

folder_path = os.path.join(cwd, folder_name)
scfolder_path=os.path.join(cwd, scfoldername)

if not os.path.exists(folder_path):
 
    os.makedirs(folder_path)
if not os.path.exists(scfolder_path):
 
    os.makedirs(scfolder_path)
    
loginpage.main()   
#creating banking application
while True:

    print(f"Welcome to {bank.bank_name}".center(40))

    optn=input(f"1.Open a new account \n2.Open a Existing account\n3.Bank information\n4.List of customers\n5.Close an Account\n6.Close application\n ")
    

    os.system('cls')
    if optn=='1':
        name=input("Enter Customer name: ")
        if len(name)<2:
            print("Invalid Name!")
        else:
            mob=input("Enter Customer mobile Number: ")
            cust=Account(name,mob)
            
            with shelve.open(r'bankdata\AccountFile') as actfile:
                actfile[cust.account_number]=cust
            
            
            os.system('cls')
            print("Account opend succesfully!!!")
            time.sleep(1)
            cust.basic_info()
            time.sleep(1)
        x=input("Press any key to continue!!!")
        os.system('cls')
        
    elif optn =='2':
        id=input("Enter Account number: ")
        try:
            
            with shelve.open(r'bankdata\AccountFile') as actfile:
                customer=actfile[id]
            
            while True:
                os.system('cls')
                print(f"Account N0:{customer.account_number} \t\t Customer Name:{customer.name}")
                opt=input("1.Deposite money\n2.Withdraw money\n3.Check current balance\n4.Customers Details\n5.Update Customers Detail\n6.Customers Transaction\n7.Home screen\n")
                os.system('cls')
                if opt=="1":
                    money=int(input("Enter Amount to Deposite: "))
                    customer.credit(money)
                    print("Amount Credited!")
                    time.sleep(1)
                
                elif opt=="2":
                    print(f"Amount available-{customer.bank_balance}")
                    money=int(input("Enter Amount to Withdraw: "))
                    customer.debit(money)
                    print("Amount debited!")
                    time.sleep(1)
                    
                elif opt=="3":
                    customer.current_balance()
                    input()
                    
                elif opt=="4":
                    customer.full_info()
                    time.sleep(1)
                    inp=input("Press any key to continue..")
                    
                elif opt=="5":
                    date=input("Enter DOB(DD/MM/YYYY): ")
                    sex=input("Enter sex(M/F): ")
                    Addr=input("Enter you Address: ")
                    customer.account_info(date,sex,Addr)
                    os.system('cls')
                    print("Account details updated succesfully!!!")
                    time.sleep(1)
                elif opt=="6":
                    transactions=customer.passbook
                
                    if len(transactions)==0:
                        print("No Transactions Available!")
                    else:
                        print("Transactions          Date                 Closing")
                        print('_'*50)
                        for t in transactions:
                            print(f"{t[0]:<10}     {t[1]:<20}   {t[2]:<10}")
                    pprint=input("Type email To get transaction email:-").lower()
                    if pprint=='email':
                        try:
                            email=input("Enter you Email address: ")
                            TranactionPdfConvertor.print_trnsaction(customer.account_number)
                            pathadd=f"pdfs\\{str(customer.name)+str('transactions.pdf')}"
                            send_email(email,pathadd)
                        except:
                            print("Can't complete your request!")
                        
                elif opt=='7':
                    break
                else:
                    print("Invalid request!")
                    time.sleep(1)
                    continue
                
            with shelve.open(r'bankdata\AccountFile') as actfile:
                actfile[id]=customer 
                actfile.sync() 
        except:
            print("Invalid Account number!") 
        
            
    elif optn=='3':
        bank.bank_info()
        time.sleep(1)
        inp=input("press any key to continue..")
        
    elif optn=='4':
        with shelve.open(r'bankdata\AccountFile') as actfile:
            bank_cust=actfile
            if len(bank_cust)==0:
                print("Zero customers available! ")
            else:
                for m in bank_cust.values():
                    print(f"{m.account_number} : {m.name}")
            input('_______________________________________\npress any key to continue....')
            os.system('cls')
    elif optn=='5':
        id=input("Enter Account number: ")
        try:
            
            with shelve.open(r'bankdata\AccountFile') as actfile:
                customer=actfile[id]
            
            while True:
                os.system('cls')
                print(f"Account N0:{customer.account_number} \t\t Customer Name:{customer.name}")
                customer.current_balance()
                customer.full_info()
                comnd=input("Confirm Deletation!\nEnter del to delete or press any key to cancel!").lower()
                if comnd=='del':
                    with shelve.open(r'bankdata\AccountFile') as actfile:
                        del actfile[id]
                        print("Account Delected Succesfully!")
                        time.sleep(1)
                else:
                    print("deletation canceled!")
                    time.sleep(1)
                os.system('cls')
                break    
                
        except:
            print("Invalid Account number!")   
    elif optn=='6':
        break
    else:
        print("Invalid request!")
        time.sleep(1)
        os.system('cls')
        continue
   
os.system('cls')
print("Thank you for Visiting LENA bank\nApko hai dena hame hai lena")
input()
time.sleep(1)   
    

    
           
    
    
    


    