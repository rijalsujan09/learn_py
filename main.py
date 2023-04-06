print("Hello world!")
if 5 > 8:
    print("five is greater than Eight!")
else:
    print("five is less than eight!")

# This is a comment.

print("--------------------------------")
# Creating variables in python..
age = 5   # age is of type int
name = "Sujan Rijal"  # name is of type string
print("Age is ", age)
print("name is ", name)

print("--------------------------------")
# Casting
x = str(3)  # x will be string '3'
y = int(3)  # y will be 3 (int)
z = float(3)  # z will be type float (3.0)
# let see the result
print(type(x))
print(type(y))
print(type(z))

#  String variable can be stored in both single and double quotation
e = "string"
e = 'string'
# both are same

print("--------------------------------")
# is  also  case-sensitive
q = 56
Q = "John Doe"
# here Q will not overwrite q
print(q)
print(Q)

print("--------------------------------")
# Multi-Word variable name
# Camel Case
myVariableName = "Sujan Rijal"
# Pascal case
MyVariableName = "Sujan Rijal"
# Snake Case
my_variable_name = "Sujan Rijal"
# -----lets print------
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

print("--------------------------------")
#  many values to multiple variables
e, f, g = "Mango", "Banana", "Orange"
print(e)
print(f)
print(g)


print("------------one value to multiple variable--------------------")
# we can also assign one value to multiple variable
k = l = m = "multiple variable one value"
print(k)
print(l)
print(m)

print("------------- Unpack Collection-------------------")
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)
print(fruits)

print("-------------Global Variable-------------------")
msg = "I am a active learner"
m = "I am outside function"
print(m)
def myFunc():
    msg = "I am a Java Dev."
    global m
    m = "I am changed to global variable.."
    print(msg, "(--Sujan Rijal)")
    print(m)
# we can also use global keyword if we want to change global variable inside function
myFunc()

print(msg)
print(m)

print("-------------Global Variable-------------------")



