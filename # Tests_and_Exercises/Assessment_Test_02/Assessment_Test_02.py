# ==============================================================================
#* 1.
# ==============================================================================

st = 'Print only the words that start with s in this sentence'
#st_list = st.split(' ')
#print(type(st))
#print(type(st_list))

print("Ex 1:")
for word in st.split(" "):
    if (word[0] == 's') or (word[0] == 'S'):
        print(word)
#    else:
#       pass

# ==============================================================================
#* 2.
# ==============================================================================
print("Ex 2:")
for num in range(0,11) :
    if num % 2 == 0:
        print(num)

# ==============================================================================
#* 3.
# ==============================================================================
print("Ex 3:")
can_divide_by_three = [num for num in range(0,51) if num % 3 == 0]
print(can_divide_by_three)

# ==============================================================================
#* 4.
# ==============================================================================

print("Ex 4:")
st2 = 'Print every word in this sentence that has an even number of letters'
#st_list2 = st.split(" ")
for word in st2.split(" "):
    if len(word) % 2 == 0:
        print(f"Even! ({word} - {len(word)} letter)")
        
# ==============================================================================
#* 5.
# ==============================================================================

print("Ex 5:")
for num in range (1,101):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
# ==============================================================================
#* 6.
# ==============================================================================

st3 = 'Create a list of the first letters of every word in this string'
#st_list3 = st3.split(" ")

letters_list = [letters[0] for letters in st3.split(" ")]
print(letters_list)