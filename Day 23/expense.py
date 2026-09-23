def add_expense(expenses,amount):
    return expenses.append(amount)

def total_expense(expenses):
    return sum(expenses)

def average_expense(expenses):
    if not expenses:
        return 0
    return sum(expenses)/len(expenses)

def main():
    expenses = []

    add_expense(expenses, 500)
    add_expense(expenses, 250)
    add_expense(expenses, 1000)
    add_expense(expenses, 750)

    print("Expenses:", expenses)
    print("Total:", total_expense(expenses))
    print("Average:", average_expense(expenses))

if __name__=="__main__":
    main()