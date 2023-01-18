
#? =============================================================================
#* 008 - Sets
#? =============================================================================

#* Unordered collection if unique elements

my_set = set()

print("empty set: {}".format(my_set))

# Adding element

my_set.add(1)
print("Added and item to the set: {}".format(my_set))
my_set.add(1)
my_set.add(1)
my_set.add(1)
my_set.add("new item")
print("Adding the same item has no effect, sets contains only unique items: {}".format(my_set))

# ==============================================================================
#* List conversion
# ==============================================================================

my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,'four',"four","five"]
converted = set(my_list)
print("list before the set conversion: {}".format(my_list))
print("list after the set conversion: {}".format(converted))

print(set("Mississippi"))