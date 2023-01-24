
#? =============================================================================
#* 014 - For loops
#? =============================================================================

"""
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
"""

my_list = [0,1,2,3,4,5,6,7,8,9]

for number in my_list:
    print(number)
    
for number in my_list:
    print("hello")
    
for number in my_list:
    print(len(my_list)-(1+number))
    
for number in my_list:
    print(my_list[::-1])
    
for number in my_list:
    if (number % 2 == 0):
        print(number)
        
#even or odd
for number in my_list:
    if (number % 2 == 0):
        print("Even number {}".format(number))
    else:
        print("Odd number {}".format(number))
        
#sum

sum_of_numbers = 0
for num in my_list:
    sum_of_numbers = sum_of_numbers + num
    #Running tally (futó összesítés)
    print("The sub-total of my_list is: {}".format(sum_of_numbers))    
print("The sum of my_list is: {}".format(sum_of_numbers))

# ==============================================================================
#* String iteration
# ==============================================================================

my_string = "Hello Zsolt"
for letter in my_string:
    print(letter)
# ==============================================================================
#* Unused cyclic variable: _
# ==============================================================================

for _ in "Hello":
    print("COOL!")

# ==============================================================================
#* Tuple iteration
# ==============================================================================

tup = (1,2,3)

for item in tup:
    print(item)

# ==============================================================================
#* Tuple unpacking!
# ==============================================================================

t_list = [(1,2),(3,4),(5,6),(7,8)]
print(f"The lenght of the tuple list: {len(t_list)}")
print("Tuplelist items:")
for item in t_list:
    print(item)
    
#* UNPACKING
print("Tuple unpacking:")
for (a,b) in t_list:
    print(a)
    print(b)
print("Tuple unpacking:")
#* no parentesis needed    
for a,b in t_list:
    print(a)
    print(b)
print("Tuple unpacking(only 'a' items):")
for a,b in t_list:
    print(a)

# ==============================================================================
#* Dictionary iteration
# ==============================================================================

d = {'k1':1, 'k2':2, 'k3':3}
print("Dictionary iteration:")
for item in d.items():
    print(item)
    
# ==============================================================================
#* Dictionary unpacking!
# ==============================================================================
print("Dictionary unpacking(values):")
for key,value in d.items():
    print(value)
    
print("Dictionary unpacking(keys):")
for key,value in d.items():
    print(key)

print("only the values:")    
for value in d.values():
    print(value)