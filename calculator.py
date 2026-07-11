def add ( a,b):
    return a+b
def sub (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    print("\n1. Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    print("5.Exit")

    choice=input("Choose:")
    if choice=="5":
        print("Calculator closed")
        break
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if choice=="1":
            print ("Answer =", add (num1,num2))
        elif choice=="2":
            print("Answer =", sub(num1,num2))
        elif choice=="3":
            print("Answer =", multiply(num1,num2))
        elif choice=="4":
            print("Answer=", divide(num1,num2))
        else:
            print("Invalid choice")   
    except:
        print("Please enter the numbers only")            

    

