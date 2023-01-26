
#? =============================================================================
#* 001 - Numbers
#? =============================================================================

number_01 = 20
number_02 = 3

# ==============================================================================
#* Arithmetic operatiors: ADDITION, SUBSTRACTION, MULTIPLICATION, DIVISON
# ==============================================================================

print (number_01 , " + " , number_02, " = " ,(number_01 + number_02))
print (number_01 , " - " , number_02, " = " ,(number_01 - number_02))
print (number_01 , " * " , number_02, " = " ,(number_01 * number_02))
print (number_01 , " / " , number_02, " = " ,(number_01 / number_02))

# ==============================================================================
#* Arithmetic operatiors: MODULUS
# ==============================================================================

print (number_01 , " % " , number_02, " = " ,(number_01 % number_02), " is the remainder")

# ==============================================================================
#* Arithmetic operatiors: EXPONENTIATION, FLOOR DIVISION
# ==============================================================================

print (number_01 , " ** " , number_02, " = " ,(number_01 ** number_02))
print (number_01, " ** 0.5 = ", (number_01 ** 0.5) )
print (number_01 , " // " , number_02, " = " ,(number_01 // number_02))

print("2 + 10 * 10 + 3 = ", 2 + 10 * 10 + 3)
print("(2 + 10) * 10 + 3 = ", (2 + 10) * 10 + 3)

# ==============================================================================
#* Floating Point Arithmetic ( Binary and Decimal Approximation)
#* https://docs.python.org/3/tutorial/floatingpoint.html
# ==============================================================================

a = 0.1
b = 0.2

print("a + b = ", a+b)