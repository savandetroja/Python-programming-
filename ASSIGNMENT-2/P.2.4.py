#4. Function with Default Arguments.Write a function to calculate simple interest.Keep rate default as 5%.

def simple_interest(p,t,r=5):
    si = (p * r * t) /100
    return si

#main program

principal = float(input("Enter principle Amount: "))
time = float(input("Enter Time (in years): "))

result = simple_interest(principal,time)

print("simple interest is",result)
