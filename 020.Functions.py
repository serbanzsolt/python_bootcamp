
#? =============================================================================
#* 020 - Functions
#? =============================================================================

"""
def name_of_the_function():

def- definition of the function
name_of_the_function- name of the function, USE snake casing!
() - parameters and arguments of the function
: - colon indicates upcoming indentation block
""" """ - multiline string comment to describe the function. Its called Docstring

"""

def say_hello():
    print("Hello")
    
say_hello()

def say_hello(name = "Default"):
    print(f"Hello {name}")
    
say_hello("Jelly")
say_hello()

def add_num (num1, num2):
    return num1 + num2

add_num(10,20)

result = add_num(10,20)
print(result)