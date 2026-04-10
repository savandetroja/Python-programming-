# 5. Write a function inside another function.

def calculate (a,b): #Definition of function
    def add():
        return a + b
    def multiply():
        return a *b

    print("Addition : ",add())
    print("multipliction :",multiply())

calculate(6,6)
