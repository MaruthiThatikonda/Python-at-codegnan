def transfer(users,sender: int, receiver: int, transfer_amount: int):

    if receiver in users:

        curr_amount = users[sender]['balance']

        if curr_amount >= transfer_amount:

            users[sender]['balance'] -= transfer_amount
            users[receiver]['balance'] += transfer_amount

            return f"{transfer_amount} Transfer successful.\nCurrent Balance is {users[sender]['balance']}"

        return "Insufficient balance"

    return "Receiver account not found"