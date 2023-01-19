
#? =============================================================================
#* 007 - Tuples
#? =============================================================================

# Tuples are like Lists but they are inmutable

my_tuple = (1,2,3)
my_list = [1,2,3]

print("Type of my_tuple: {}".format(my_tuple))

# It can has mixed object type just like a list

my_tuple02 = (1,'two',3.14)
print("tuple with mixed obj type: {}".format(my_tuple02))
print("Indexing and slicing tuples: {}".format(my_tuple02[1:]))

# ==============================================================================
#* Methods - only 2 method available
# ==============================================================================

#* count()

letters_tuple = ("a", "b", "a", "c")
print("Counting the letter 'a' in the tuple: {}".format(letters_tuple.count("a")))

#* index() - returns the passed value very first time appear in the tuple

print("The first time 'b' appear in the tuple at: {}".format(letters_tuple.index("b")))

# ==============================================================================
#* Inmutability
# ==============================================================================

letters_tuple[0] = 'new'