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
y = x.title() #AbcABC title makes the first lette capitalized
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