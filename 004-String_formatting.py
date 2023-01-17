
#? =============================================================================
#* 004 - String formatting
#? =============================================================================

# ==============================================================================
#* String Interpolation: .format() method
# ==============================================================================

print("The {} {} {}".format("fox","brown","quick"))
print("The {2} {1} {0}".format("fox","brown","quick"))
print("The {0} {0} {0}".format("fox","brown","quick"))
print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))

# ==============================================================================
#* Float formatting: "{value:width.precision f}"
# ==============================================================================

result = 100/777
print("result: ", result)

print("the result was {}".format(result))
print("the result was {r}".format(r=result))
print("the result was {r:1.3f}".format(r=result))
print("the result was {r:10.3f}".format(r=result))

# ==============================================================================
#* String Interpolation: f-strings (Formatted String Literals)
# ==============================================================================

name = "Zsolt"
print(f"Hello, my name is {name}")

name_02 = "Sam"
age = 10

print(f"His name is {name_02} and he is {age} years old")