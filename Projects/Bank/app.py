from login import login
from balance import balance
from withdraw import withdraw
from deposite import deposite
from transfer import transfer
from ministatement import ministatement
from logout import logout


# user table 
users = {
    1234:{'name':"koushik","Email":"maruthithatikonda00@gmail.com@gmail.com","balance":5000,"password":"1234"},
    1235:{'name':"Shreyas","Email":"maruthithatikonda00@gmail.com","balance":10000,"password":"1235"},
    }

# services
def register(name:str, email:str, initial_deposite:int, password:str):
    print("you are in register page")
    


# main
if __name__=="__main__":

    print("Welcome to the Small Scale Bank")
    print("1.Register \n 2.Login")
    choice= int(input(" Select Your Choice:"))

    # calling register function
    if choice == 1:
        print("Registration page under development process....")

    # calling login function    
    elif choice==2:
        account = int(input("Enter your Account Number"))
        password = input("Enter your Password:")
        login_val = login(users, account, password)

        while login_val:
            print("The Small scale Bank Providing services")
            print("1. Balance \n 2. Withdraw \n 3. Deposite \n \
                  4. Transfer \n 5. Ministatement \n 6. Logout")
            choice=int(input("Enter your choice(1-6):"))

            if choice == 1:
                # call balance function
                current_balance = balance(users, account)
                print(f"Current Balance is :{current_balance}")
            elif choice == 2:
                # call amount
                amount = int(input("Enter your withdraw amount:"))
                # call withdraw function
                res = withdraw(users, account, amount)
                print(res)

            elif choice == 3:
                # call deposit amount
                amount = int(input("Enter your deposit amount:"))
                # call deposit function
                res = deposite(users, account, amount)
                print(res)

            elif choice == 4:
                # receiver account
                receiver = int(input("Enter Receiver Account Number:"))
                # transfer amount
                amount = int(input("Enter Transfer Amount:"))
                # call transfer function
                res = transfer(users, account, receiver, amount)
                print(res)

            elif choice == 5:
                # call mini statement function
                res = ministatement(account=account)
                print(res)

            elif choice == 6:
                # call logout function
                res = logout()
                print(res)
                break

            else:
                print("Invalid Choice! Please select between 1 and 6.")

        print("invaild login credientials")
    else:
        print("choose option 1 or 2")
   





