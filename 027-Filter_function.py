
#? =============================================================================
#* 027 - Filter function
#? =============================================================================

def check_even(number):
    return number % 2 == 0

my_numbers = [1,2,3,4,5,6]

print( list(filter(check_even, my_numbers)) )
