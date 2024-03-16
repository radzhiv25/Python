# case 

x = int(input("Enter value of x: "))

match x:
    case 0:
        print("X is zero")
    case _ if (x > 0):
        print("X is positive")
    case _:
        print("X is negative")


# for loop

# for loop in a string  
a = "Rajeev"
for i in a:
    print(i)

# for loop in a list
colors = ['Red', 'Green', 'Blue', 'Yellow']
for color in colors:
    print(color)

# for loop with range
# here stop value will be always 1 less than as mentioned
for i in range(4): # default start is 0
    print(i)
for j in range(1,10): # start and stop are defined
    print(j)
for k in range(1,20,4): # (start, stop, step)
    print(k)