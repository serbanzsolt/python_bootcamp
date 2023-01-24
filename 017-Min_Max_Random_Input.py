
#? =============================================================================
#* 017 - Min, Max, Random, Input
#? =============================================================================

# ==============================================================================
#* Min,Max
# ==============================================================================

mylist = [10,20,30,40,100]
minimum = min(mylist)
maximum = max(mylist)

print(mylist)
print("The minimum of this list is {}".format(minimum))
print("The maximum of this list is {}".format(maximum))

# ==============================================================================
#* Random
# ==============================================================================

#* Importing from a library
from random import shuffle

ordered_list = [1,2,3,4,5,6,7,8,9]
print("Here is a list with ordered items: {}".format(ordered_list))

shuffled_list = shuffle(ordered_list)
#* shuffle() in an in-place function, shuffled_list will return None!

print("After shuffled the list: {}".format(ordered_list))

#* Importing from a library
from random import randint

some_random_integer = randint(1,100)
print("Here is some random integer: {}".format(some_random_integer))

# ==============================================================================
#* Input
# ==============================================================================

result = input("Enter a number here! ")
print("The input you gave is: {}".format(result))

result2 = input("Favourite number: ")
print("The type of the input field is: {}".format(type(result2)))

result2 = int(result2)
print("After the type conversion: {} and the type: {}".format(result2, type(result2)))