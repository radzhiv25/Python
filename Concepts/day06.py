a = int(input("Enter your age :"))
# types of condtional <, >, <=, >=, ==, !=

# if-else statement
if(a > 18):
    print("You can drive") # here indentation is important
else:
    print("You can't drive")

# elif statement
b = int(input("Enter the number:"))
if(b > 0):
    print("The number is positive")
elif(b == 0):
    print("The number is zero")
else:
    print("The number is negative")

# nested if-else statement with elif statement
c = int(input("Enter the number:"))
if(c < 0):
    print("Number is negative")
elif(c > 0):
    if(c < 10):
        print("The number is between 1-10")
    elif(c > 10 and c <= 20):
        print("The number is between 10-20")
    elif(c > 20):
        print("The number is greater than 20")
else:
    print("The number is zero")