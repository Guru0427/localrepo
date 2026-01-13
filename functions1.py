# functions without parameters
def greetings():
    print("welcome")
greetings()

# 2..
# function to adds two numbers and print result.
def addnumbers(a,b):
    result=a+b
    print("the sum is: ",result)
# call the above  sum function
addnumbers(46,85)

# the return statement is used in a function to send the result back to the place where the function was called.
# def add(a,b)
# return a+b
# result=add(65,85)
# print(result) 

# function to convert celsius to fahrenheit
def cel_to_far(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print(cel_to_far(25))


# THE PASS SATATEMENT
# The pass satatement is a placeholder in a function or loop.It does nothing and is used when you need to write code that will be added later or to define an empty function.

# def myfunction():
pass # This does nothing for now.