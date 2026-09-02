# Today we learn about exception handling in Python. Exception handling allows us to manage errors gracefully and prevent our programs from crashing unexpectedly. In Python, we use the `try`, `except`, `else`, and `finally` blocks to handle exceptions.
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input! Please enter a valid integer for your age.")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
try:
    sum_result = a + b
    print(f"The sum of {a} and {b} is: {sum_result}")
except Exception as e:
    print(f"An error occurred: {e}")

numbers = [10, 20, 30, 40]
try:
    index=int(input("Enter index: "))
    print(f"The number at index {index} is: {numbers[index]}")
except IndexError:
    print("Index out of bounds! Please enter a valid index.")
except Exception as e:
    print(f"An error occurred: {e}")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
try:
    division_result = a / b
    print(f"The result of {a} divided by {b} is: {division_result}")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print("Division performed successfully.")

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("Execution completed. Thank you for using the program.")

try:
    password = input("Enter your password: ")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    print("Password accepted.")
except ValueError as ve:
    print(f"Error: {ve}")

try:
    number=int(input("Enter a number: "))
    if number <= 0:
        raise ValueError("Number must be positive.")

    print(f"You entered a positive number: {number}")
except ValueError as ve:
    print(f"Error: {ve}")

#Temperature Converter
try:
    temp_celsius = float(input("Enter temperature in Celsius: "))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F.")
except ValueError:
    print("Invalid input! Please enter a valid number for the temperature.")

#Shopping Cart
try:
    item_price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))
    total_cost = item_price * quantity
    print(f"The total cost for {quantity} items is: ${total_cost:.2f}")
except ValueError:
    print("Invalid input! Please enter valid numbers for price and quantity.")

#Number Password
try:
    password = input("Enter a numeric password: ")
    if not password.isdigit():
        raise ValueError("Password must be numeric.")

    print("Password accepted.")
except ValueError as ve:
    print(f"Error: {ve}")

#Percentage Calculator
try:
    total_marks = float(input("Enter total marks: "))
    obtained_marks = float(input("Enter obtained marks: "))
    if total_marks <= 0:
        raise ValueError("Total marks must be greater than zero.")
    percentage = (obtained_marks / total_marks) * 100
    print(f"Your percentage is: {percentage:.2f}%")
except ValueError as e:
    if obtained_marks > total_marks:
        print("Obtained marks cannot be greater than total marks.")
except ValueError as ve:
    print(f"Error: {ve}")

#Custom Exception
try:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account_balance = 1000.0  # Example account balance
    if withdraw_amount > account_balance:
        raise ValueError("Insufficient funds in the account.")
except ValueError as ve:
    print(f"Error: {ve}")

import datetime
#Date Validator
try:
    date_input = input("Enter a date (YYYY-MM-DD): ")
    date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    print(f"You entered a valid date: {date_object.date()}")
except ValueError:
    print("Invalid date format! Please enter the date in YYYY-MM-DD format.")