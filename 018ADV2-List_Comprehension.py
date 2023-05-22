
#? =============================================================================
#* LIST Comprehension Advanced Exercises 2
#? =============================================================================

# ==============================================================================
#* Find all of the numbers from 1-1000 that are divisible by 7
# ==============================================================================
print("Case 1:")

result1 = [number for number in range(1,1000) if number % 7 == 0]
print(result1)

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Find all of the numbers from 1-1000 that have a 3 in them
# ==============================================================================
print("Case 2:")

result2 = [number for number in range(1,1000) if "3" in str(number)]
print(result2)

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Count the number of spaces in a string
# ==============================================================================
print("Case 3:")

my_string = "There are some spaces in this string"
result3 = [space for space in my_string if space == " "]
print(len(result3))

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Create a list of all the consonants in the string 
#* “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
# ==============================================================================
print("Case 4:")

string_with_consonants = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
result4 = [con for con in string_with_consonants.lower() if con not in ("a,e,i,o,u")]
print(result4)

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
#* Result would look like (index, value), (index, value)
# ==============================================================================
print("Case 5:")

my_list5 = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result5 = [tuple((index, value) for index, value in enumerate(my_list5))]
print(result5)

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
# ==============================================================================
print("Case 6:")

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
result6 = [a for a in list_a if a in list_b]
print(result6)

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
# ==============================================================================
print("Case 7:")

sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
words = sentence.split()
result7 = [num for num in words if num.isnumeric()]
print(result7)

print("--------------------------------------------------------------------------")
# ==============================================================================
#* Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even,
#* and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
# ==============================================================================
print("Case 8:")

result8 = ["even" if n%2 == 0 else "odd" for n in range(20)]
print(result8)
'''
List comprehension
[expression for item in list]
expression = "'even' if n %2 == 0 else 'odd'"
for item in list = "for n in range(20)"
'''
print("--------------------------------------------------------------------------")
# ==============================================================================
#* Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12.
#* Result would look like (4,4), (12,12)
# ==============================================================================

list_a9 = 1, 2, 3,4,5,6,7,8,9
list_b9 = 2, 7, 1, 12

result10 = [(a,b) for a in list_a9 for b in list_b9 if a==b]
print(result10)

# ==============================================================================
#* Find all of the words in a string that are less than 4 letters
# ==============================================================================
sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'

examine = sentence.split()

result = [word for word in examine if len(word) <4]
print(result)
# ==============================================================================
#* Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# ==============================================================================


#old school
no_dups = set()
for n in range(1, 100):
  for x in range(2,10):
    if n % x == 0:
      no_dups.add(n)
print(no_dups)
print()

#nested list comprehension

result = [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
print(result)




