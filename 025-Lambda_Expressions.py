
#? =============================================================================
#* 025 - Lambda expressions
#? =============================================================================

def square (num):
    result = num ** 2
    return result

print(square(3))

#* Turning it to a lambda expression:

sqr = lambda num: num ** 2

print(sqr)
print(sqr(2))