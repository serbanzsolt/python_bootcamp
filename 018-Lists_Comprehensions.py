
#? =============================================================================
#* 018 - Lists Comprehensions
#? =============================================================================

"""
[expression for item in iterable if condition]

expression:     the expression that we apply to the collected elements
item:           variable that we iterate through the iterable object
iterable:       the array, list, or other object that we iterate through
condition:      is the condition by which we filter the elements
"""

numbers = [1,2,3,4,5]

sum = [x**2 for x in numbers if x%2==0]
print(sum)

# Celsius > Farenheit

celsius = [0, 10, 20, 34.5]
print(f"The list of celsius: {celsius}")

farenheit = [(9/5*temp+32) for temp in celsius]
print(f"The list of farenheit: {farenheit}")

#* without list comprehension:

farenheit = []
for temp in celsius: 
    farenheit.append(((9/5)*temp+32))
print(farenheit)

# ==============================================================================
#* If...Else list comprehension (bad coding not readable!!!)
# ==============================================================================

result = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(result)

# ==============================================================================
#* Nested for loops comprehension
# ==============================================================================
mylist = []

for x in [2,4,6]:
    for y in [100, 200, 300]:
        mylist.append(x*y)
        
print(mylist)

mylist2 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist2)