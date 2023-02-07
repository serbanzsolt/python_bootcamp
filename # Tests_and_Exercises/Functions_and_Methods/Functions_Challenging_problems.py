
#? =============================================================================
#* Functions and Methods: Challenging PROBLEMS
#? =============================================================================
def result_print(result):
    print("The result: {}".format(result))   

def title(title):
    print("\n{}\n".format(title))
    
# ==============================================================================
#* SPY GAME: Write a function that takes in a list of integers
#* and returns True if it contains 007 in order
# ==============================================================================
title("SPY GAME")

def spy_game(nums):
    if (nums.count(0) >= 2) and (nums.count(7) >= 1):
        
        pass
    else:
        return False

mylist = [1,0,3,21,0,12,3,1,7]
print(mylist.count(0))
zeroes = []
sevens = 0
for index,item in enumerate (mylist):
    print(f"index: {index}  item: {item}")
    if item == 0:
        zeroes.append( (index, item) )
print(zeroes)
