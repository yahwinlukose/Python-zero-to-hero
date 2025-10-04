operator=input("Enter an operator (+, -, *, /): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if operator=='+':
    print(round(num1+num2))
elif operator=='-':
    print(round(num1-num2))            
elif operator=='*':
    print(round(num1*num2))
elif operator=='/':
    if num2!=0:
        print(num1/num2)
    else:
        print("Error: Division by zero")
else:
    print(f"{operator} is  an Invalid operator")            
