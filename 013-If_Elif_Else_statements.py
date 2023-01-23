
#? =============================================================================
#* 013 - If Elif Else statements
#? =============================================================================

"""
if some_condition:
    execute some code
elif some other condition:
    do something different
else:
    do something else
"""

hungry = False
if hungry:
    print("Feed me!")
else:
    print("I'm not hungry")

hungry = True
if (hungry==True) :
    print("Feed me!")
else:
    print("I'm not hungry")
    
loc = "Bank"

if loc == "Auto Shop":
    print("Cars are cool!")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Store":
    print("Welcome to the Store!")
else:
    print("I do not know much")
