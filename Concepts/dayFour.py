# here we learn about input function
a = input()
print("My name is :", a)

x = input("Enter a number: ")
y = input("Enter another number: ")
result = int(x) + int(y) # else it will concatenate the two numbers
print(result)

# string
name = "John"
# a string is like array of characters
surname = 'Doe'
desc = """
He is a specialist in AI and ML.
He is a good programmer.
He is famous for his work in the field of AI.
"""

print(name + " " + surname)
print(name[2])
print(desc)
print(name*3)

for character in name:
    print(character)

# string slicing and operations

fruit = "Mango"
fruitLen = len(fruit)
print('Mango is a', fruitLen, "letter word")
# here we will see positive and negative slicing
vegetable = "Potato"
print(vegetable[0:6]) # here 0 is inclusive and 6 is exclusive
print(vegetable[:6]) # here 0 is inclusive and 6 is exclusive
print(vegetable[0:]) # here 0 is inclusive and 6 is exclusive
print(vegetable[1:]) # here 1 is inclusive and 6 is exclusive
print(vegetable[2:-1]) # for negative slicing the negative value is subtracted from the length of the string
print(vegetable[-5:-2])

nm = "Harry"
print(nm[-4:-2])
print(len(nm))