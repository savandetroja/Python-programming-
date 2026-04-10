#1. Write a Function to Perform Arithmetic Operations.Create separate functions for addition,
#subtraction, multiplication, and division. Call them based on user input.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if  b==0:
        return "Error"
    return a/b

print("select operation =")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice = input("Enter your choice :")

a=int(input("Enter a first value :"))
b=int(input("Enter a second value :"))

if choice=='1':
    print("result =",add(a,b))
elif choice=='2':
    print("result =",sub(a,b))
elif choice=='3':
     print("result =",mul(a,b))
elif choice=='4':
    print("result =",div(a,b))
else:
    result = "Invalid choice !"
