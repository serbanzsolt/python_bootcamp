# ==============================================================================
#* Value swapping
# ==============================================================================

level = "Archer"
role = 45
#assigned wrong, correction:
level, role = role, level

print(f"Level: {level}\nRole: {role}")

# ==============================================================================
#* join()
# ==============================================================================

inventory = [
    "Iron Sword",
    "Health Potion",
    "Wooden Shield",
    "Stick"
]

print(f"\nYou have: {', '.join(inventory)}")

# ==============================================================================
#* Line Continuation
# ==============================================================================

a_variable = True
b_variable = True
c_variable = False

if a_variable == True and b_variable == True and c_variable == False:
    print("oneline")
    
if a_variable == True \
    and b_variable == True \
        and c_variable == False:
    print("multiline")
    
# ==============================================================================
#* any() function
# ==============================================================================

enemies = [
    {"type" : "ork", "health" : 0},
    {"type" : "ork", "health" : 0},
    {"type" : "ork", "health" : 5},
    {"type" : "ork", "health" : 4}
]

if any(enemy["health"] for enemy in enemies):
    print("the battle goes on!")
else:
    # if all health is 0
    print("no more enemies left")

# ==============================================================================
#* List comprehension
# ==============================================================================

names = [
    "Bobby C. Brown",
    "Chris Stevens",
    "Jacob J. Smith",
    "John Paul Davis"
]
last = [name.split(" ")[-1] for name in names]
print(last)

# ==============================================================================
#* Dictionary comprehension
# ==============================================================================

names2 = [
    "Daniel",
    "Mike",
    "William"
]

#List comprehension:
lenghts = [len(name) for name in names2]
print(lenghts)

#Dictionary comprehension:
lenghts = {name : len(name) for name in names2}
print(lenghts)

# ==============================================================================
#* Unpacking
# ==============================================================================

inputs = [
    "John",
    "Smith",
    "United States",
    "blue",
    "brown",
    "29"
]

firstname, lastname, *_, age = inputs
print(f"{firstname} {lastname} is {age} years old")

# ==============================================================================
#* rfind() and title() methods
# ==============================================================================

x = "abcABC"
y = x.title() #AbcABC title makes the first letter capitalized
z = y.rfind("b") # rfind gives back the index of the last found item
print(z)

# ==============================================================================
#* get() method (dictionary)
# ==============================================================================

p1 = {"xp":3976, "level":3}
p2 = {"xp":1123, "level":1}
p3 = {"xp":0} # new player no level yet

player_db = [p1, p2, p3]
for p in player_db:
    lvl = p.get("level", 0) #second argument here is the default when there is no data
    print(f"Level: {lvl}")
    
# ==============================================================================
#* raise()
# ==============================================================================

user_input = 10 # If odd, error is raised
if user_input % 2 == 1:
    err = "Must be even number of players"
    raise Exception(err)

team_a_size = user_input / 2
team_b_size = team_a_size

print(f"Team A: {team_a_size} players")

# ==============================================================================
#* insert()
# ==============================================================================

x = [1,2,3]
x.insert(4, 3) # insert (where, what) index for is not exist 
                #so it automatically will be the last one
print(x)

# ==============================================================================
#* Floor Division
# ==============================================================================

x = [4, -5, 6]
y = lambda x: abs(x//2)
z = list(map(y, x))
print(z)

# ==============================================================================
#* Recursion
# ==============================================================================

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(7))

# ==============================================================================
#*remove()
# ==============================================================================

x = [1,2,3,2,1]
x.remove(2) # remove will remove the item in () but only the first it finds
y = sum(x)
print (y)

# ==============================================================================
#* Python Carets ^
# ==============================================================================

x = "b001"
y = [x.find("0")]
z = len(y)^2 # ^ exclusive or -> 1^2 binary -> 11 binary is 3 in decimal
print(z)

# ==============================================================================
#* title()
# ==============================================================================

first = "bOB"
second = "sMITH"

name = f"{first} {second}"
print(f"Your name is: {name.title()}.")
