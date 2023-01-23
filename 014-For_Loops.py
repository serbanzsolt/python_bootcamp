
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
        

for number in my_list:
    if (number % 2 == 0):
        print("Even number {}".format(number))
    else:
        print("Odd number {}".format(number))