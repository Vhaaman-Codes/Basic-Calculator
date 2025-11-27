num1=float(input("Enter any number: "))
operator=input("Choose an operator...  For addition(\"+\")  For subraction(\"-\")  For multiplication(\"*\")  For division(\"/\"): ")
num2=float(input("Enter another number: "))

if operator== "+":
    print(float(num1+num2))
elif operator== "-":
    print(float(num1-num2))
elif operator== "*":
    print(float(num1*num2))
elif operator== "/":
    print(float(num1/num2))
else:
    print("Invalid Operator!")
