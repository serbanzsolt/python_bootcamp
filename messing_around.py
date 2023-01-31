# ==============================================================================
#* Pick Evens
#*
#* Define a function called myfunc that takes in an arbitrary number of arguments,
#* and returns a list containing only those arguments that are even.
# ==============================================================================

def myfunc (*args):
    results = []
    for item in args:
        if item % 2 == 0:
            results.append(item)
    else:
        pass
    return results

result_list = myfunc(1,2,3,4,5,6,7,8,9,11,12,1232,33333)
print(result_list)

# ==============================================================================
#* SKYLINE
#*
#* Define a function called myfunc that takes in a string,
# *and returns a matching string where every even letter is uppercase,
# *and every odd letter is lowercase. 
# *Assume that the incoming string only contains letters,
# *and don't worry about numbers, spaces or punctuation. 
# *The output string can start with either an uppercase or lowercase letter,
# *so long as letters alternate throughout the string.
# ==============================================================================

def myfunc2 (word):
    word = word.lower()
    result = ""
    for i in range(0, len(word)):
        if i % 2 == 1:
            result += word[i].upper()
        else:
            result += word[i]
    return result

print(myfunc2("appleinthegarden"))
print(myfunc2("CAPITALLETTERS"))