# 🎯 Mini Calculator CLI
# Build a calculator that asks:
# First number
# Operator (+, -, *, /)
# Second number
# Performs the calculation and displays the result.
# If operator is invalid, print “Invalid operator”.

# This pure my code --> yup lot things to refine back
def title():
    banner= ''' Welcome to Mini Calculator '''
    print(banner)


def run():
    num = []
    for i in range(1,3):
        no =input(f"Enter your number {i}: ")
        number = int(no)
        if i == 1:
            num.append(number)
            num1 = num[0]
        elif i ==2:
            num.append(number)
            num2 = num[1] 

            operate = input(f"Choose operator: ")
            print(f"Workflow: {num1} {operate} {num2}")
            if operate == "+": 
                add = num1 + num2
                print(f"Total:{add}")
            elif operate == "-":
                if num1 > num2:
                    sub = num1 - num2
                else:
                    sub = num2 - num1
                print(f"Total: {sub}")
            elif operate == "*":
                mult = num1 * num2
                print(f"Total: {mult}")
            elif operate == "/":
                div1 = num1 / num2
                div2 = num2 /num1
                print(f"Type 1: {div1}\nType 2: {div2}")
            else:
                print(f"Invalid operator:  {operate}")
        #else:
         #   break    
        
title()
run()

#this what AI suggest and refine 

def title():
    banner = ''' Welcome to Mini Calculator '''
    print(banner)

def run():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    operator = input("Choose operator (+, -, *, /): ")

    print(f"Workflow: {num1} {operator} {num2}")

    if operator == "+":
        print(f"Total: {num1 + num2}")
    elif operator == "-":
        print(f"Total: {num1 - num2}")
    elif operator == "*":
        print(f"Total: {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Total: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")

title()
run()
