# # Arguments in functions
# #1.. Required arguments(single/multiple)

# def greetings(name):   #   name is parameter
#     print("hello",name)

# greetings("banty")   # banty is argument

# #2.. Default arguments

# def greetings(name="world"):    #  world is the default value
#     print("hello",name)
# greetings()    # runs without error using default value

# greetings("banty")


# # 3.. Keyword arguments( named argument)

# def divide(a,b):
#     return a/b
# result=divide(100,20)
# print(result)

# result1=divide(100,20)   # positional arguments
# print(result1)

# result2=divide(b=100,a=20)   # named arguments
# print(result2)


# #4...
# # Arbitary positional arguments(*args)

# # If you are unsure how many arguments will be passed use (*args) to accept any number of positional arguments.
# # Allows you to pass a variable number of positional arguments.
# # The arguments are stored as a tuple.
# # Use when you want to pass multiple values that are accessed by position.

# def add_numbers(*args):
#     return sum(args)
# result=add_numbers(1,2,3,4)
# print(result)

# # 5..
# # Arbitary keyword arguments(**kwargs)

# # If you want to pass a variable number of keywords arguments,use **kwargs .
# # The arguments are stored as a dictionary.
# # Use when you want to pass multiple values that are accessed by name.

def print_details(**kwargs):
    # print (type(kwargs))    # dictionary type
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(name="Banty",age=26,city="delhi")


