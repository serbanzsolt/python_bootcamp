
#? =============================================================================
#* 018 Advanced - List Comprehension
#? =============================================================================

# ==============================================================================
#* Example: Fruits
# ==============================================================================

fruits = ["apples", "bananas", "strawberries"]

for fruit in fruits:
    print(fruit)

print("\nUsing list comprehension:")

[print(fruit) for fruit in fruits]

# ==============================================================================
#* Example: Upper fruit
# ==============================================================================

fruits = ["apples", "bananas", "strawberries"]
new_fruits = []

for fruit in fruits:
    fruit = fruit.upper()
    new_fruits.append(fruit)
    
fruits = new_fruits
print("\nUpperCase fruits:")
print(fruits)

print("\nUsing list comprehension:")
new_fruits_2 = [fruit.upper() for fruit in fruits]
print(new_fruits_2)

# ==============================================================================
#* Example: SuperBits
# ==============================================================================

bits = [False, True, False, False, True, False, False, True]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

super_bits = [1 if b == True else 0 for b in bits]

print("\nBits:")
print(bits)
print("\nNew Bits:")
print(new_bits)
print("\nSuper Bits")
print(super_bits)

# ==============================================================================
#* Example: String Manipulation
# ==============================================================================
print("\nString manipulation:\n")
my_string = "HelloMyNameIsZsolt"
print(my_string)
my_string = [ i for i in my_string ]
print(my_string)
my_string = "".join([ i for i in my_string ])
print(my_string)

my_string = "HelloMyNameIsZsolt"
my_string = "".join(
    [i if i.islower() else " " + i for i in my_string]
    )[1:]
print(my_string)

my_string = "HelloMyNameIsZsolt"
my_string = "".join([i if i.islower() else " " + i.lower() if i in ["M", "I", "N"] else " " + i for i in my_string])[1:]
print(my_string)

# ==============================================================================
#* Example: squares
# ==============================================================================

squares = []

for i in range(1,101):
    squares.append(i**2)
print("\nSquares 1-101")
print(squares)

print("\nUsing list comprehension")
squares2 = [i**2 for i in range(1,101)]
print(squares2)

# ==============================================================================
#* Example: Remainders
# ==============================================================================

remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5)

for i in range(0, len(remainders5)):
    if remainders5.count(i) != 0:
        print(f"There are {remainders5.count(i)} pieces of {i} remainder in range ")

print("\nUsing list comprehension:")
        
[print(f"There are {remainders5.count(i)} pieces of {i} remainder in range ") for i in range(0, len(remainders5)) if remainders5.count(i) != 0]

remainders11 = [ x**2 % 11 for x in range(1,101) ]
print(remainders11)

# ==============================================================================
#* Example: G-Movies
# ==============================================================================

movies = ["Star Wars", "Ghandi", "Shawshank Redemption", "Gattaca", "Groundhog day"]

g_movies = []
for title in movies:
    if title.startswith("G"):
        g_movies.append(title)
print("\nG-movies:")
print(g_movies)

gmovies = [ title for title in movies if title.startswith("G")]
print("\nUsing list comprehension:")
print(gmovies)

# ==============================================================================
#* Pre2K
# ==============================================================================

movies = [
    ("Citizen Kane", 1941),
    ("Spirited Away", 2001),
    ("Gattaca", 1997),
    ("Raiders of the lost ark", 1981),
    ("The Aviator", 2004)
]
print("\nMovies:")
print(movies)
pre2k = [title for (title, year) in movies if year < 2000]
print(f"\nmovies before 2000: {pre2k}")

# ==============================================================================
#* Scalar Multiplication
# ==============================================================================

vector = [2, -3, 1]
print(f"\nscalar multiplication: {vector} x4:")
vector_4x = [v*4 for v in vector]
print(vector_4x)

# ==============================================================================
#* Cartesian Product (René Descartes - Descartes sorozat(hun))
# ==============================================================================

A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)

# ==============================================================================
#* Multi Dimensional lists
# ==============================================================================
print("\nMulti dimensional lists:")

x = [i for i in range(10)]
print(x)

x = [i for i in range(10) if i % 2 == 0]
print(x)

x = [(i, y) for i in range(10) for y in range(20)]
print(x)

x = [[] for i in range(10)]
print(x)

x = [[0 for i in range(5)] for i in range(10)]
print(x)

x = [[True for i in range(5)] for i in range(10)]
print(x)

x = [[[0 for i in range(5)] for i in range(2)] for i in range(2)]
print(x)