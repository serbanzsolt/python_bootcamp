
#? =============================================================================
#* 002 - Variable Assignment
#? =============================================================================

"""Rules for variable names
names can not start with a number
names can not contain spaces, use _ intead
names can not contain any of these symbols:

      :'",<>/?|\!@#%^&*~-+
       
it's considered best practice ([PEP8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)) that names are lowercase with underscores
avoid using Python built-in keywords like `list` and `str`
avoid using the single characters `l` (lowercase letter el), `O` (uppercase letter oh) and `I` (uppercase letter eye) as they can be confused with `1` and `0`
"""

# ==============================================================================
#* Assignment Operator " = "
# ==============================================================================

a = 10

print ("a: ", a)

#Reassign Variable:
a = a + 10

print ("a: ", a)
print ("Type of a: ", type(a))

my_income = 100
tax_rate = 0.27
my_taxes = my_income * tax_rate

print("My taxes: ", my_taxes)
print("Type of my taxes: ", type(my_taxes))