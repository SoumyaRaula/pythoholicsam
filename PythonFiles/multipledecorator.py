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

# Multiple Decorators


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "Hello , Mr. {0}. Good Morning".format(name)


print (get_text('Charlie'))
