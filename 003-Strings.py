
#? =============================================================================
#* 003 - Strings
#? =============================================================================

# ==============================================================================
#* Quotes
# ==============================================================================

word_01 = 'Hello'
word_02 = "Zsolt"
print(word_01, word_02)
print("I'am Zsolt") #single quotes can used in double quotes

# ==============================================================================
#* Concatenation
# ==============================================================================

word_03 = word_01 + word_02
print(word_03)

word_03 = word_01 + " " + word_02
print(word_03)

# ==============================================================================
#* len() - Built-in function
# ==============================================================================

word_lenght = len('My name is Zsolt')
print("lenght of the string 'My name is Zsolt' is", word_lenght)

# ==============================================================================
#* Escape sequences
# ==============================================================================

print("New \nLine")
print("using \ttab")

# ==============================================================================
#* Indexing
# ==============================================================================

mystring = "Hello World"

print("First character of my string is:", mystring[0])
print("8th character of my string is:", mystring[8])
print("Using reverse indexing:", mystring[-3])

# ==============================================================================
#* Slicing
#* mystring[start:stop:step]
# ==============================================================================

my_abc = "abcdefghijk"
print(my_abc[2:])
print(my_abc[:3])
print(my_abc[3:6])
print(my_abc[::-1])

my_reversed_abc = my_abc[::-1]
print(my_reversed_abc)

# ==============================================================================
#* Built-in Methods
# ==============================================================================

x = "Hello Zsolt"
print(x.upper())
print(x.lower())

print(x.split())
y = x.split()
print(type(y))

long_string = "Hi this is a long string"
print(long_string.split())
print(long_string.split("i"))