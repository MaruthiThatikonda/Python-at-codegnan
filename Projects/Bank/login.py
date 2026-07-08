# register or login
def login(users,account:int, password:str)->bool:
    #calling login function
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False