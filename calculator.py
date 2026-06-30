import math
print("Program Started")
print("=== Professional Calculator===")
def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return"Error! Division by zero is not allowed."
    return a / b
def modulus(a,b):
    return a % b
def power(a,b):
    return a ** b
def square(a):
    return a**2
def square_root(a):
    if a < 0:
        return "Error ! Square root of a negative number is not possible."
    return math.sqrt(a)
def percentage(a,b):
    return(a/b)*100

def menu():

    print("\n==== PROFESSIONAL CALCULATOR====")
    print("1.Addition(+)")
    print("2.Substraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Modulus(%)")  
    print("6.Power(x^y)")
    print("7.Square(x)")
    print("8.Square Root(x)")    
    print("9.Percentage")
    print("10.Exit")
    print("==========================")
while True:
        print("Inside Loop")
        menu()
        choice=input("Enter your choice(1-10):")
        if choice =="10":
            print("Thank you for using Professional Calulator")
            break
        if choice in["1", "2", "3", "4","5","6","7","8","9"]:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            if choice == "1":
                result=add(num1,num2)
            elif choice == "2":
                result=substract(num1,num2)
            elif choice =="3":    
                result=multiply(num1,num2)
            elif choice =="4":
                result=divide(num1,num2)    
            elif choice =="5":
                result=modulus(num1,num2)
            elif choice =="6":
                result=power(num1,num2)
            elif choice =="7":
                num=float(input("Enter number:"))
                result=square(num)
            elif choice =="8":
                num=float(input("Enter your number:"))
                result=square_root(num)
            elif choice =="9":
                result=percentage(num1,num2)
            else:
                print("Invalid choice Please try again.")
                continue
            print("Result=",result)    

                               

