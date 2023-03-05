
#? =============================================================================
#* Homework - Errors and Exceptions: Problem 1
#? =============================================================================

#* Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# for i in ['a','b','c']:
#     print(i**2)


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Type error, please provide a number instead!")
# else:
#     print("There was no error!")

