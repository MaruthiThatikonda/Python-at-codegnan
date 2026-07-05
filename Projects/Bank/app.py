
# user table 
users = {
    1234:{'name':"Maruthi","Email":"maruthithatikonda00@gmail.com","balance":5000,"password":"1234"},
    1235:{'name':"Shreyas","Email":"shreyasiyer96@gmail.com","balance":10000,"password":"1235"},
    }

# services
def register(name:str, email:str, initial_deposite:int, password:str):
    print("You are in Register page")

# register or login
def login(account:int, password:str)->bool:
    # chaeck account exist in user or not
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False
    

# balance function defination
def balance(account:int)->int:
    current_amount=users[account]['balance']
    return current_amount

# withdraw function defination
def withdraw(account:int, withdraw_amount:int)->str:
    curr_amount= users[account]['balance']
    # check amount
    if curr_amount >=withdraw_amount:
        users[account]['balance'] -=withdraw_amount
        return f"{withdraw_amount} withdrawal succesful and \
            Current Balance is {users[account]['balance']}"
    return "Insuccifent balance"

# deposite function defination
def deposite(account:int, deposite_amount:int):
        users[account]['balance'] +=deposite_amount
        return f"{deposite_amount} Deposite succesful and \
            Current Balance is {users[account]['balance']}"
    
    

#transfer function defination
def transfer(sender:int, reciever:int, transfer_amount:int):
    if receiver in users:
        curr_amount= users[sender]['balance']
        if curr_amount >=transfer_amount:
            users[sender]['balance'] -= transfer_amount
            users[receiver]['balance'] = transfer_amount
            return f"{transfer_amount} Transfer succesful and \
            Current Balance is {users[sender]['balance']}"
        return "Insuffient Balance"
    return "Reciever account not found"



# ministatement function defination
def ministatement(account:int):
    return "Mini statement is under development"

# logout function defination
def logout():
    return "ThankYou for using Small scale bank, See You Again...."

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
        login_val = login(account=account, password=password)

        while login_val:
            print("The Small scale Bank Providing services")
            print("1. Balance \n 2. Withdraw \n 3. Deposite \n \
                  4. Transfer \n 5. Ministatement \n 6. Logout")
            choice=int(input("Enter your choice(1-6):"))

            if choice == 1:
                # call balance function
                current_balance=balance(account=account)
                print(f"Current Balance is :{current_balance}")
            elif choice == 2:
                # call amount
                amount = int(input("Enter your withdraw amount:"))
                # call withdraw function
                res = withdraw(account=account, withdraw_amount=amount)
                print(res)

            elif choice == 3:
                # call deposit function
                amount = int(input("Enter your deposit amount:"))
                # call deposit function
                res = deposite(account=account, deposite_amount=amount)
                print(res)

            elif choice == 4:
                # receiver account
                receiver = int(input("Enter Receiver Account Number:"))
                # transfer amount
                amount = int(input("Enter Transfer Amount:"))
                # call transfer function
                res = transfer(sender=account, reciever=receiver, transfer_amount=amount)
                print(res)

            elif choice == 5:
                # call mini statement function
                # amount =int(input("Enter a"))
                res = ministatement(account=account)
                print(res)

            elif choice == 6:
                # call logout function
                print(logout())
                exit()

            else:
                print("Invalid Choice! Please select between 1 and 6 choices.")

        print("Invalid Login cerdentials")
    else:
        print("Invalid chioce. Please select choice 1 or 2.")
   





