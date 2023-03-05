
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
    idx_zeroes = []
    idx_sevens = []
    for index, item in enumerate(nums):
        if item == 0:
            idx_zeroes.append(index)
        elif item == 7:
            idx_sevens.append(index)
            
    if len(idx_zeroes) >= 2 and len(idx_sevens) >=1:
        if idx_zeroes[-1] < idx_sevens[-1]:
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

# ==============================================================================
#* More elegant way...
# ==============================================================================

def spy_g (nums):
    
    code = [0,0,7,"x"]
    for num in nums:
        if num == code[0]:
            code.pop(0)
            # before pop [0,0,7,"x"]
            # [0,7,"x"]
            # [7,"x"]
            # ["x"] length is 1
    
    if len(code) == 1:
        return True
    else:
        return False
    
result = spy_g(list1)
result_print(result)

result = spy_g(list2)
result_print(result)

result = spy_g(list3)
result_print(result)

result = spy_g(list4)
result_print(result)

result = spy_g(list5)
result_print(result)

result = spy_g(list6)
result_print(result)

result = spy_g([1,2,4,0,0,7,5])
result_print(result)

result = spy_g([1,0,2,4,0,5,7])
result_print(result)

result = spy_g([1,7,2,0,4,5,0])
result_print(result)