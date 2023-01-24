
#? =============================================================================
#* 016 - Range, Enumerate, Zip, In
#? =============================================================================

mylist = [1,2,3]
# ==============================================================================
#* Range
# ==============================================================================
"""
range(start,stop,step)
"""

print("range(10):")
for num in range(10):
    print(num)
    
print("range(2,10):")
for num in range(2,10):
    print(num)
    
print("range(2,10,2):")
for num in range(2,10,2):
    print(num)

r_list = list(range(0,11,2))
print(r_list)
# ==============================================================================
#* Enumerate
# ==============================================================================

index_count = 0

for letter in "abcde":
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

# Common solution
index_count = 0

word = "abcde"
for letter in word:
    print(word[index_count])
    index_count += 1
    
#* using Enumerate
for item in enumerate(word):
    print(item)

#* using Enumerate and Tuple unpacking
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")
    
# ==============================================================================
#* Zip
# ==============================================================================

my_list1 = 1,2,3
my_list2 = ["a","b","c"]

print("Zipping 2 lists together:")
for item in zip(my_list1, my_list2):
    print(item)

my_list1 = 1,2,3
my_list2 = ["a","b","c"]
my_list3 = [100,200,300]

print("Zipping 3 lists together:")
for item in zip(my_list1, my_list2, my_list3):
    print(item)
    
#casting it a zip
zip_list = list(zip(my_list1,my_list2,my_list3))
print("zipped into a list: {}".format(zip_list))

# ==============================================================================
#* In
# ==============================================================================

result = 2 in [1,2,3]
print(result)

result2 = "x" in ["x","y","z"]
print(result2)

result3 = "mykey" in {"mykey" : 345}
print(result3)

d = {"mykey" : 345}

print(345 in d.values())
print(345 in d.keys())