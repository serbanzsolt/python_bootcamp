
#? =============================================================================
#* 005 - Lists
#? =============================================================================

my_list01 = [1,2,3]
my_list02 = ['dog', 100, 23.4]

print ("my_list02 has {itemlen} items".format(itemlen=len(my_list02)))

my_list03 = ['one','two','three']

print("mylist03's second item is '{}'".format(my_list03[1]))
print("mylist03's last 2 items are {}".format(my_list03[1:]))

# ==============================================================================
#* List concatenation
# ==============================================================================

my_list04 = ["four", "five", "six"]

print("Two list concatenated: {}".format( my_list03 + my_list04 ))

# ==============================================================================
#* Mutate elements
# ==============================================================================

my_list04[0] = "Changed the first element"
print(my_list04)

# ==============================================================================
#* List Methods
# ==============================================================================

#Add item to the list
new_list = ['one', 'two', 'three', 'four']
print("newlist = {}".format(new_list))
new_list.append("five")
print("newlist after append = {}".format(new_list))

#Remove item from a list
fruits = ['apple', 'pear', 'banana', 'kiwi']
print("fruits list = {}".format(fruits))

popped_item = fruits.pop()
print("fruits list after used pop method = {}".format(fruits))
print("The popped item is: {}".format(popped_item))
fruits.pop(0)
print("fruits list after poped first item = {}".format(fruits))

#Sorting a list
letters = ['z', 'a', 'f', 'b', 'c']
numbers = [99,1,32,4,10]

print("letters list: {}".format(letters))
print("numbers list: {}".format(numbers))

letters.sort()
numbers.sort()

print("letters list after sort() method: {}".format(letters))
print("numbers list after sort() method: {}".format(numbers))

#Common Error!
my_sorted_list = numbers.sort()
print("my sorted list : {}".format(my_sorted_list))
print("type of my sorted list : {}".format(type(my_sorted_list)))

#Reverse
numbers.reverse()
print("number list after reverse() method: {}".format(numbers))