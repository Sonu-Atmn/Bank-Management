import shelve
import os
bankcode='12345'
def add_user():
    print("User Registration!")
    user_id=input("Enter a New ID:")
    name=input("Enter your name: ")
    while True:
        code=input("Enter bank code: ")
        if code == bankcode:
            break
        else:
            print("Wrong bank code!")
    
    
    while True:       
        password=input("Create password: ")
        cpassword=input("Confirm password: ")
        if cpassword!=password:
            print("password and confirm password doesn't match!")
            input("Enter again!")
        else:
            break
        
    with shelve.open(r'bankdata\bankuser') as userfile:
        if user_id in userfile:
            print(f"{user_id} already registered please use another Id!")
            input()
        else:
            userfile[user_id]={'name':name,'password':password}
        print("User added succesfully!")
        input()
    
def user_login():

    print("Login")
    
    with shelve.open(r'bankdata\bankuser') as file:
        user_id=input("Enter user_id: ")
        password=input("Enter password: ")
        if user_id not in file:
            print("User not Registered! ")
            input()
            return False
        else:
            if password == file[user_id]['password'] :
                print(f"welcome {file[user_id]['name']}")
                input()
                return True
            else:
                print("invalid userid  or password!")
                input()
                return False
            
def main():           
    while True:
        os.system('cls')               
        print("welcome to Lena Bank\n\n")
        opt=input("1.Login To bank\n2.User registration\n")
        if opt=='1':
            os.system('cls')
            status=user_login()
            if status:
                break
        elif opt=='2':
            os.system('cls')
            add_user()
        else:
            print("Unknown request!")
    os.system('cls')

if __name__=='__main__':
    main()
    