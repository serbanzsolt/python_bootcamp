
#? =============================================================================
#* 026 - Map functions
#? =============================================================================
#* DATA: a1, a2, a3...aN
#* Funtion: f
#* map (f, data):
#*      returns iterator over
#*      f(a1), f(a2), ..., f(aN)

def square (num):
    return num ** 2

my_nums = [1,2,3,4,5]

# for item in my_nums:
    # print(item)
    
for item in map(square,my_nums):
    print(item)

print( list(map(square, my_nums)) )

def splicer (mystring):
    if len(mystring) % 2 == 0:
        return "Even"
    else:
        return mystring[0]

names = ["Andy", "Eve", "Sally"]

#* in here at splicer() we only pass the name, not the (),
#* we dont want to execute, map will do it. We just passing it as an argument

print(list( map(splicer,names )))

# ==============================================================================
#* Examples: Radii
# ==============================================================================

import math

radii = [2,5,7.1,0.3,10]

def area(r):
    return math.pi * (r**2)

areas = []

areas = list(map(area,radii))
print(areas)

#* same with lambda expression
areas_lambda = list(map( (lambda r: math.pi * (r**2)), radii ))
print(areas_lambda)

# ==============================================================================
#* Examples: Celsius to Fahrenheit
# ==============================================================================

temps = [
    ("Berlin", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angeles", 26),
    ("Tokyo", 27),
    ("New York", 28),
    ("London", 22),
    ("Beijing", 32)
]
print ("\nCelsius temp:")
print (temps)

c_to_f = lambda data : (data[0], (9/5) * data[1] + 32)

print ("\nFahrenheit temp:")
fahrenheits = list(map(c_to_f, temps))
print(fahrenheits)