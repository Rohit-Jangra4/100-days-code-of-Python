# Raising Custom Errors
num=int(input("Enter a number between 5 and 10: "))
if num < 5 or num > 10:
    raise ValueError("Number is not in the valid range.")
print(f"You entered a valid number: {num}")

salary=int(input("Enter your salary: "))
if salary not in range(10000, 100000):
    raise ValueError("Salary is not in the valid range.")
print(f"You entered a valid salary: {salary}")

# Question 1
num=int(input("Enter a number: "))
if num < 0:
    raise ValueError("Number cannot be negative.")
print(f"You entered a valid number: {num}")

# Question 2
try:
    age=int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be at least 18.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"You entered a valid age: {age}")

# Question 3
class CustomError(Exception):
    pass
num=int(input("Enter a number: "))
if num < 0:
    raise CustomError("Number cannot be allowed.")
print(f"You entered a valid number: {num}")

# Question 4
class CustomError(Exception):
    pass
try:
    age=int(input("Enter your age: "))
    if age < 0:
        raise CustomError("Age cannot be negative.")
    elif age >= 120:
        raise CustomError("Age must be a valid human age.")
except CustomError as e:
    print(f"Error: {e}")
else:
    print(f"You entered a valid age: {age}")    

# Question 5
class CustomError(Exception):
    pass
try:
    marks=int(input("Enter your marks: "))
    if marks<0:
        raise CustomError("Marks cannot be negative.")
    elif marks>100:
        raise CustomError("Marks cannot be greater than 100.") 
except CustomError as e:
    print(f"Error: {e}")
else:
    print(f"You entered valid marks: {marks}")

# Question 6
class CustomError(Exception):
    pass
try:
    amount=int(input("Enter the amount: "))
    balance=5000
    if amount <= 0:
        raise CustomError("Amount must be greater than 0.")

    if amount > balance:
        raise CustomError("Insufficient balance.")
except CustomError as e:
    print(f"Error: {e}")
else:
    print("Withdrawal successful.")

# Question 7
class CustomError(Exception):
    pass
try:
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    age=int(input("Enter your age: "))
    if marks < 0 or marks > 100:
        raise CustomError("Marks must be between 0 and 100.")
    if age < 0 or age > 120:
        raise CustomError("Age must be between 0 and 120.")
except CustomError as e:
    print(f"Error: {e}")
else:
    print(f"You entered valid details: Name: {name}, Marks: {marks}, Age: {age}")

# Question 8

class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


# ATM Functions

balance = 10000


def check_balance():
    print(f"Your balance is: ₹{balance}")


def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0")

    balance += amount
    print(f"₹{amount} deposited successfully.")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance -= amount
    print(f"₹{amount} withdrawn successfully.")


# Main ATM Program

while True:

    print("\n===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")

    except InvalidAmountError as e:
        print("InvalidAmountError:", e)

    except InsufficientBalanceError as e:
        print("InsufficientBalanceError:", e)