# withdraw function defination
def withdraw(users,account:int, withdraw_amount:int)->str:
    curr_amount = users[account]['balance']
    #check amount
    if curr_amount >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdrawl succesful and \
        current Balance is {users[account]['balance']}"
    return "insufficient Balance"