# deposite function defination
def deposite(users,account:int, deposite_amount:int):
    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite succesful and \
    current Balance is {users[account]['balance']}"
    