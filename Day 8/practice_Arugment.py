# 1. Sum of List
def list_sum(num):
    sum=0
    for i in num:
        sum+=i

    return sum

result=list_sum([1,2,3,4,5,6,7,8])

print("Sum of list is:",result)

# 2. Employee Salary Calculator
def salary(total_salary,allowance,deduction):
    total=total_salary+allowance-deduction
    return total


print(salary(30000,5000,2000))
        
# 3. Electricity Bill ⚡
def bill(units,rate,fixed_charge):
    total_bill=(units*rate)+fixed_charge

    print(total_bill)

bill(250,6,100)

# 4. Loan EMI 💰
def calculate_emi(principal, rate, years):
    R = rate / (12 * 100)
    N = years * 12

    emi = (principal * R * (1 + R) ** N) / ((1 + R) ** N - 1)

    return emi


principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period (years): "))

print("Monthly EMI:", calculate_emi(principal, rate, years)) 

# 5. Number Analyzer
def analyze_number(num, divisor):
    if num<0:
        print("-ve")
    elif num>0:
        print("+ve")
    else:
        print("Zero")

    if num%2==0:
        print("Even")
    else:
        print("Odd")

    if num % divisor ==0:
        print("Divisible")
    else:
        print("Not Divisible")

analyze_number(56894,7)