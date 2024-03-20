#functions 

def calculateAll(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    print(add,sub,mul,div,sep=" ")

a = int(input("Enter first numbers:"))
b = int(input("Enter second number:"))
calculateAll(a,b)