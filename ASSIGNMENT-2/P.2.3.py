#3. Function to Calculate Factorial (Using Recursion),Implement factorial using:Normal function,Recursive function

def factorial (n):
    if n < 0:
        return "Factroial does not exist for negative number"

    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

 #main program

num =int(input("Enter a number : "))
result = factorial (num)

print("Factorial (Recursive) =",result)
