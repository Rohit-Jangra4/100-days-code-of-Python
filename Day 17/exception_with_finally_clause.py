# Today we learn about finally clause in exception handling. The finally clause is used to execute code regardless of whether an exception was raised or not. It is often used for cleanup actions, such as closing files or releasing resources.
l=[1, 2, 3, 4, 5]
try:
    num=int(input("Enter a number: "))
    print(l[num])
except IndexError:
    print("Index out of bounds!")
except ValueError:
    print("Invalid input!")
finally:
    print("Cleanup actions can be performed here.")

#
def func():
    list1 = [1, 2, 3, 4, 5]
    try:
        num = int(input("Enter a number: "))
        print(list1[num])
        return 0
    except IndexError:
        print("Index out of bounds!")
        return 1

        print("This line will not be executed due to the return statement in the except block.")

x = func()
print(x)

# Question 1
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = None
finally:
    print("The result is:", result)
# Question 2
try:
    name =input("Enter your name: ")
except Exception as e:
    print("An error occurred:", e)
finally:
    print(f"Thank you {name} for using the program.")

# Question 3
try:
    integer = int(input("Enter an integer: "))
    print("You entered:", integer)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("Execution completed.",)

# Question 4
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter valid integers.")
except zeroDivisionError:
    print("Cannot divide by zero!")
finally:
    if 'num1' in locals() and 'num2' in locals():
        print("The result of the division is:", num1 / num2)

# Question 5
def test():
    try:
        return "Try"
    finally:
        print("Finally")

print(test())

# Question 6
try:
    num = int(input("Enter number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid number")

finally:
    print("Thank you for using the program")

# Question 7
try:
    file = open("index.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")

# Question 8
try:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username != "admin" or password != "password":
        raise ValueError("Invalid credentials!")
except ValueError as e:
    print(e)
finally:
    print("Execution completed.")

# Question 9
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    function = input("Enter an operation (+, -, *, /): ")
    if function == "+":
        result = a + b
    elif function == "-":
        result = a - b
    elif function == "*":
        result = a * b
    elif function == "/":
        result = a / b
    else:
        raise ValueError("Invalid operation!")
except ValueError as e:
    print(e)
finally:
    print("Calculator closed.")

#