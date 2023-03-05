
#? =============================================================================
#* Homework - Errors and Exceptions: Problem 2
#? =============================================================================

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("You cannot divide by Zero!")