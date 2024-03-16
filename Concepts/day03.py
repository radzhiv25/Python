a = 12345 # this is an integer
print(a)
b = "Python" # this is a string
c = 123.45 # this is a float
d = True # this is a boolean
e = complex(1, 2) # this is a complex number

print(b, c, d, sep= " ") 
print(a+c)
print(e)
print("The type of b: ", type(b)) 
print("The type of c: ", type(c))
print("The type of d: ", type(d))

#this is mutable
list1 = [1, 3.4, [-4,-10.343], "Python"]
print(list1)
# this is immutable
tuple1 = (['hey', 'hello'],'a')
print(tuple1)

dict1 = {'name': 'John', 'age': 25}
print(dict1)