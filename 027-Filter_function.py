
#? =============================================================================
#* 027 - Filter function
#? =============================================================================

def check_even(number):
    return number % 2 == 0

my_numbers = [1,2,3,4,5,6]

print( list(filter(check_even, my_numbers)) )

# ==============================================================================
#* Examples: Find all data above the average
# ==============================================================================

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)
print(f"Sensor data: {data}")
print(f"\nThe average to the sensor data: {avg}")

print(f"Greater than the average: {(list(filter(lambda x : x > avg, data)))}")

# ==============================================================================
#* Examples: Remove the missing data
# ==============================================================================

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(f"\nCountries with missing data: \n{countries}")

result = list(filter(None, countries))
print(f"\nRemoved the missing data: \n{result}")

# ==============================================================================
#* Using None above gives back False value.
#* False values in Python:
#*     "" - Empty String,
#*     0, 0.0, 0j - Zero,
#*     [] - Empty list,
#*     () - Empty Tuple,
#*     {} - Empty Dictionary,
#*     False - logical False,
#*     None - None variable,
#*     and instances which signal they are empty
# ==============================================================================