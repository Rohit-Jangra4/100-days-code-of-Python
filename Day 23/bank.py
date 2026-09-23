def deposit(balance,amount):
    return balance+amount

def withdrawal(balance,amount):
    if amount>balance:
        return "Unsufficient Balance"
    
    return balance-amount

if __name__=="__main__":
    balance=1000000

    Balance=deposit(balance,34000)
    print("After Deposit:",Balance)

    Balance=withdrawal(balance,14078)
    print("After Withdrawal:",Balance)

