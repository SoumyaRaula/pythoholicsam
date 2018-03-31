"""
__author__: sranjanr
__desc__: decorators
"""

"""
1. Annotation.
def function(function_arg): #base() as an argument
    perform operation on base()
    return enhanced_base() #adds functionality to the base and returns it 

@function()
def base():
    pass

2. Explicit declaration.
new_func = function(base) 
"""

# Wrapper
def function1(str1):
    def return_new(str):
        return "Hello " + str
    string_new = return_new(str1)
    return string_new

print (function1("World"))


# Decorator
def smart_divide(func):
    def inner(a,b):
        print ("Divide these :", a, b)
        if b == 0:
            print ("Cant divide this.")
        return func(a,b)
    return inner

@smart_divide
def divide(a, b):
    return (a/b)

print (divide(10,0))






