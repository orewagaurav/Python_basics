def sum(a,b):
    return a+b

def product(a,b):
    return a*b

def sub(a,b):
    return a-b

def division(a,b):
    return a/b

def remainder(a,b):
    return a%b

def power(a,b):
    return a**b

def floordiv(a,b):
    return a//b

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

print("Enter your choice:\n1)ADD\n2)Subtract\n3)Multiply\n4)Divide\n5)Remainder\n6)Power\n7)FloorDiv\n")
choice = int(input("Enter the choice (1-7): "))

if choice==1:
    print("Adding x,y is: ",sum(x,y))
elif(choice==2):
    print("Subtracting x,y is: ",sub(x,y))
elif(choice==3):
    print("Multiplying x,y is: ",product(x,y))
elif(choice==4):
    print("Dividing x,y is: ", division(x,y))
elif(choice==5):
    print("Remaindering x,y is: ",remainder(x,y))
elif(choice==6):
    print("Powering x,y is: ", power(x,y))
elif(choice==7):
    print("Floordividing x,y is: ", floordiv(x,y))