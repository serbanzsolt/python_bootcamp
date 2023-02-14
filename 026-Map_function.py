
#? =============================================================================
#* 026 - Map functions
#? =============================================================================

def square (num):
    return num ** 2

my_nums = [1,2,3,4,5]

# for item in my_nums:
    # print(item)
    
for item in map(square,my_nums):
    print(item)

print( list(map(square, my_nums)) )

def splicer (mystring):
    if len(mystring) % 2 == 0:
        return "Even"
    else:
        return mystring[0]

names = ["Andy", "Eve", "Sally"]

#* in here at splicer() we only pass the name, not the (),
#* we dont want to execute, map will do it. We just passing it as an argument

print(list( map(splicer,names )))