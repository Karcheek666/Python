
#take input from user
num1 = input("Enter first number: ")

#take second input
num2 = input("Input second number: ")

#take thr operator they want to use
op = input("Enter the operator of your choice: ")

#assign operator between inputs and get output
try:
    if op == "+":
        sum =  int(num1) + int(num2)
        print(sum)

    elif op == "-":
        difference = int(num1) - int(num2)
        print(difference)

    elif op == "x":
        product = int(num1) * int(num2)
        print(product)

    elif op =="/":
        quotient = int(num1) / int(num2)
        print(quotient)
        
except ValueError as vale:
    print("Please input appropriate values.")
    
# Add alert for wrong operator input 
for letter in op:
    if letter in ("x","/","+","-"):
        print("All Okay!")
    else:
        print("Invalid Operator.")

