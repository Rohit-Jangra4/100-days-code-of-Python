# Question 1

day=int(input("Day:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invaild day.")

# Question 2

x=int(input("X:"))
y=int(input("Y:"))
rule=input("Enter the function which do you perform [+,-,*,/]:")
match rule:
    case "+":
        print(f"Addition of {x} and {y} is: {x+y}")
    case "-":
        print(f"Subtraction of {x} and {y} is:{x-y}")
    case "*":
        print(f"Multiplication of {x} and {y} is:{x*y}")
    case "/":
        print(f"Division of {x} and {y} is:{x/y}")

# Question 3

color=input("Enter traffic light color:")
match color:
    case "red":
        print("Stop🖐️")
    case "green":
        print("Go🫡")
    case "Orange":
        print("stop for a minute")
    case _:
        print("invalid color")

# Question 4

user_choice=input("Give order from this menu [pizza,burger,pasta,Exit]:")
match user_choice:
    case "pizza":
        print("Order is Pizza")
    case "burger":
        print("Order Bureger")
    case "pasta":
        print("Order Pasta")
    case _:
        print("Exit.....")

# Question 5
num=int(input("Enter the number form (1 to 5):"))
match num:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case 4:
        print("4")
    case 5:
        print("5")

    