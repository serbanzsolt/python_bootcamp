
#? =============================================================================
#* Functions and Methods: Challenging PROBLEMS - SPYGAME
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
    zeroes = []
    sevens = []
    for index, item in enumerate(nums):
        if item == 0:
            zeroes.append(index)
        elif item == 7:
            sevens.append(index)
            
    if len(zeroes) >= 2 and len(sevens) >=1:
        if zeroes[-1] < sevens[-1]:
            return True
        else:
            return False
    else:
        return False

list1 = [0,2,3,0,32,1]
list2 = [1,3,2,7,123,7,99]
list3 = [0,32,0,1,0,7]
list4 = [0,0,7]
list5 = [1,0,3,21,0,12,3,1,7]
list6 = [0,0,0,0,0,7]

result = spy_game(list1)
result_print(result)

result = spy_game(list2)
result_print(result)

result = spy_game(list3)
result_print(result)

result = spy_game(list4)
result_print(result)

result = spy_game(list5)
result_print(result)

result = spy_game(list6)
result_print(result)

result = spy_game([1,2,4,0,0,7,5])
result_print(result)

result = spy_game([1,0,2,4,0,5,7])
result_print(result)

result = spy_game([1,7,2,0,4,5,0])
result_print(result)
