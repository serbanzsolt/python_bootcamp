
#? =============================================================================
#* 015 - While Loops
#? =============================================================================

"""
while some_boolean_condition:
    #do something
"""
x = 0

while x < 5:
    print(f"The current value of x is: {x}")
    x = x + 1
    # x += 1
else:
    print ("X is not less than 5")
    
# ==============================================================================
#* LOOP Keywords: BREAK, CONTINUE, PASS
# ==============================================================================

"""
break: Break out of the current closest enclosing loop
continue: Goes to the top of the closest enclosing loop
pass: Does nothing at all
"""

# ==============================================================================
#* pass
# ==============================================================================
# for loop cannot be empty
print("pass:")
x = [1,2,3]

for item in x:
    #comment
    pass

print("End of the script")

# ==============================================================================
#* continue
# ==============================================================================
print("continue:")
mystring = "Zsolt"

for letter in mystring:
    if (letter == 'o'):
        continue
        # GO to the top of the closest enclosing loop
    print(letter)

# ==============================================================================
#* break
# ==============================================================================
print("break:")
for letter in mystring:
    if (letter == 'o'):
        break
        # Breaks out the closest enclosing loop
    print(letter)
