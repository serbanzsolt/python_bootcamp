
#? =============================================================================
#* 021 - Logic with functions
#? =============================================================================

def even_check (number):
    result = number % 2 == 0
    return result

"""
def even_check (number):
    return number % 2 == 0

"""
print(even_check(41))
print(even_check(20))

# ==============================================================================
#* return true if any number is even in a list
# ==============================================================================

def is_even(list):
    for number in list:
        if number % 2 == 0:
            return True
        else:
            pass
        
result_list = is_even([1,2,3])
print(f"Result_list: {(result_list)}")

result_list2 = is_even([1,1,3])
print(f"Result_list2: {(result_list2)}")

result_list3 = is_even([1,1,1,2])
print(f"Result_list3: {(result_list3)}")

result_list4 = is_even([2,1,1,1])
print(f"Result_list4: {(result_list4)}")

def check_even_list(list):
    for number in list:
        if number % 2 == 0:
            return True
        else:
            #return false >>> THIS IS WRONG!!!!!!
            pass
    return False #Have to be carefull with the correct indentation

# ==============================================================================
#* return all the even numbers in a lsit
# ==============================================================================

def is_even_list(list):
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list

my_list = is_even_list( [ 1,2,3,4,5,6,7,8 ] )
print(f"The even list: {my_list}")

my_list2 = is_even_list( [ 1,3,5 ] )
print(f"The even list2: {my_list2}")