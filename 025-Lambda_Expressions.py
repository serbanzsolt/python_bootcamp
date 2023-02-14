
#? =============================================================================
#* 025 - Lambda expressions
#? =============================================================================
#* use:
#*     1 - lambda keyword 
#*     2 - followed by 0 or more inputs
#*     3 - followed by a colon :
#*     4 - followed by Single Expression
#* Lambda usually called Anonymous Function, they are the same
#* Usually called when the function is used only one time
#* CANNOT USE: multiline functions, expressions

def square (num):
    result = num ** 2
    return result

print(square(3))

#* Turning it to a lambda expression:

sqr = lambda num: num ** 2

print(sqr)
print(sqr(2))

# ==============================================================================
#* Examples: inline uses
# ==============================================================================

my_nums = [1,2,3,4,5]

#* ex 1
print ( list(map(lambda num: num ** 2, my_nums)) )

#* ex 2
print( list( filter(lambda num: num % 2 == 0, my_nums) ) )

#* ex 3
names = ["Andy", "Eve", "Sally"]
print(list(map(lambda x:x[0], names)))
#* variable name can be anything
print(list(map(lambda name:name[0], names)))

print(list(map(lambda name:name[::-1], names)))

# ==============================================================================
#* Example: Sci-Fi Authors
# ==============================================================================
#* Mission: sort the list by last name

scifi_authors = [
    "Isaac Asimov",
    "Ray Bradbury",
    "Robert Heinlein",
    "Arthur C. Clarke",
    "Frank Herbert",
    "Orson Scott Card",
    "Douglas Adams",
    "H. G. Wells"
    "Leigh Brackett"
]
# help(scifi_authors.sort)

print("Authors list: (unsorted)")
print(scifi_authors)

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print("\nAuthors sorted by their last name:")
print(scifi_authors)

# ==============================================================================
#* Example: Quadratic Functions (a*x2 + bx + c)
# ==============================================================================
#* Computing cannonball trajectories

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x : a*x**2 + b*x + c

f = build_quadratic_function(2,3, -5)

print( f(0) )
print( f(1) )
print( f(2) )

print(build_quadratic_function(3,0,1)(2))