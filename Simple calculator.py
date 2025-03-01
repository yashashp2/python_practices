#Simple calculator

num1 = int(input("Enter the first operand: "))
num2 = int(input("Enter the second operand: "))
operator = input('Enter a operator("*","/","+","-","%"): ')
total = 0
if operator == '*':
    total = num1 * num2
    print(f"The product of {num1} and {num2} is {total}")

elif operator == '/':
    total = num1 / num2
    print(f"The quotient of {num1} and {num2} is {round(total,2)}")

elif operator == '+':
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")

elif operator == '-':
    total = num1 - num2
    print(f"The difference of {num1} and {num2} is {total}")

else:
    total = num1 % num2
    print(f"The remainder of {num1} and {num2} is {total}")
