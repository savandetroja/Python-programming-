#2. Function to Find Largest of Three Numbers.Accept three numbers as parameters.Return the largest number.

# Fuction Definition

def lagest(a,b,c):
    if a >=b and a >=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

 # main program

num1 =float(input("Enter first number : "))
num2=float(input("Enter second number :"))
num3=float(input("Enter third number :"))

result =lagest(num1,num2,num3)

print("Largest number is ",result)                 
