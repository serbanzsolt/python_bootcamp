
#? =============================================================================
#* Functions and Methods: LEVEL 2 PROBLEMS
#? =============================================================================

def result_print(result):
    print("The result: {}".format(result))   

def title(title):
    print("\n{}\n".format(title))
    
# ==============================================================================
#* FIND 33: 
#* Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# ==============================================================================
title("FIND 33")

def has_33(nums):
    for i in range(1,(len(nums)-1)):
        if ( (nums[i] == 3) and ((i > 0) and (i < (len(nums))))):
            if (nums[i] == nums[i-1]) or (nums[i] == nums[i+1]):
                return True
            else:
                pass
        else:
            pass
    return False

result = has_33([1, 3, 3])
result_print(result)

result = has_33([1, 3, 1, 3])
result_print(result)

result = has_33([3, 1, 3])
result_print(result)

result = has_33([3, 3, 1])
result_print(result)

result = has_33([3, 3, 1, 1, 1, 1, 1, 1, 3, 3])
result_print(result)

# ==============================================================================
#* PAPER DOLL: Given a string, return a string 
#* where for every character in the original there are three characters
# ==============================================================================
title("PAPER DOLL")

def paper_doll(text):
    text_return = ""
    for i in range(0, len(text)):
        text_return += (text[i]*3)
    return text_return

result = paper_doll('Hello')
result_print(result)

result = paper_doll('Mississippi')
result_print(result)

# ==============================================================================
#* BLACKJACK: Given three integers between 1 and 11,
#* if their sum is less than or equal to 21, return their sum.
#* If their sum exceeds 21 *and* there's an eleven,
#* reduce the total sum by 10. 
#* Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# ==============================================================================
title("BLACKJACK")

def blackjack(a,b,c):
    bj = [a,b,c]
    sum_bj = sum(bj)
    if (11 in bj) and (sum_bj >21):
        return (sum_bj-10)
    elif sum_bj > 21:
        return "BUST"
    elif sum_bj <= 21:
        return sum_bj
    else:
        print("wrong input")
        

result = blackjack(5,6,7)
result_print(result)

result = blackjack(9,9,9)
result_print(result)

result = blackjack(9,9,11)
result_print(result)

result = blackjack(6,7,8)
result_print(result)

# ==============================================================================
#* SUMMER OF '69: Return the sum of the numbers in the array,
#* except ignore sections of numbers starting with a 6 and extending to the next 9
#* (every 6 will be followed by at least one 9). Return 0 for no numbers.
# ==============================================================================
title("SUMMER OF 69")

def summer_69(arr):
    if (6 in arr) and (9 in arr):
        six_pos = arr.index(6)
        nine_pos = arr.index(9)
        if (six_pos < nine_pos):
            subs_list = []
            for i in range(six_pos,nine_pos+1):
                #print(arr[i])
                subs_list.append(arr[i])
            return (sum(arr) - sum(subs_list))
        else:
            return sum(arr)
    else:
        return sum(arr)

result = summer_69([1, 3, 5])
result_print(result)

result = summer_69([9, 5, 32, 7, 8, 6])
result_print(result)

result = summer_69([4, 5, 6, 7, 8, 9])
result_print(result)

result = summer_69([2, 1, 6, 9, 11])
result_print(result)