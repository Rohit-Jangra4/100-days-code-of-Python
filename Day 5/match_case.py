# Match case latest added in python version 3.10

# Example 1

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

# Example 2

status=404

match status:
    case 200:
        print("Success")
    case 400|404:
        print("Client Error")
    case 500:
        print("Server Error")
    case _:
        print("invaid status.")
    
# Example 3

data=[1,2]
match data:
    case [x,y]:
        print(f"Two elements {x} and {y}")
    case [x]:
        print(f"One element {x}")
    case _:
        print("Something else.")

# Example 4

age=int(input("Age:"))
match age:
    case x if x<=13:
        print("child")
    case y if x>=20 and x<=59:
        print("Adult")
    case z if x>=60:
        print("Senior citizen")
    case _:
        print("Teenager")

# Example 5

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