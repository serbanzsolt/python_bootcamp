
#? =============================================================================
#* 006 - Dictionaries
#? =============================================================================

#* {'key1':'value1','key2':'value2'}

new_dict = {'key1' : 'value1', 'key2' : 'value2'}
print("new_dict : {}".format(new_dict))

prices_lookup = {'apple' : 2.99, 'oranges' : 1.99, 'milk' : 5.80}
print("Milk price from dictionary: {}".format(prices_lookup['milk']))

d = {'k1' : 123, 'k2' : [0,1,2], 'k3':{'insideKey':100}}

print("d: {}".format(d))
print("k2: {}".format(d['k2']))
print("InsideKey: {}".format(d['k3']['insideKey']))

# ==============================================================================
#* Mutable
# ==============================================================================

abc = {'key1' : ['a','b','c']}

abc_list = abc['key1']
print("abc_list: {}".format(abc_list))

letter = abc_list[2]
print("Letter in uppercase: {}".format(letter.upper()))

# Solution in one line
print(abc['key1'][2].upper())

# ==============================================================================
#* Add new item
# ==============================================================================

my_dict = {
    'k1' : 'value1',
    'k2' : 'value2',
    'k3' : 'value3'
}
print(my_dict)

my_dict['k4'] = 'value4'
print(my_dict) 

# ==============================================================================
#* Methods
# ==============================================================================

print("Only the keys: {}".format(my_dict.keys()))
print("Only the values: {}".format(my_dict.values()))
print("Items of the dictionary: {}".format(my_dict.items()))