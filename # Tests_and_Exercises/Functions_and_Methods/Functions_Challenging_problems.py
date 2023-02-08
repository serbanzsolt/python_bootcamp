
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

# mylist = [1,0,3,21,0,12,3,1,7]
# print(mylist.count(0))
# for i in range(0,len(mylist)):
#     if i == 0:
#         for j in range(i,len(mylist)):
#             if j == 0:
#                 for k in range(j, len(mylist)):
#                     if k == 7:
#                         print(">>> 007 <<<") 

# def spy_game_007 (num_list):
#     for index1, item1 in enumerate(num_list):
#         if item1 == 0:
#             # print(f"I found 0 on FIRST level in location: {index1}")
#             for index2, item2 in enumerate(num_list[index1+1:]):
#                 if item2 == 0:
#                     # print(f"I found 0 on SECOND level in location: {num_list.index(0,index1+1)}")
#                     for index3, item3 in enumerate(num_list[index1+2:]):
#                         if item3 == 7:
#                             # print(f"I found 7 on THIRD level in location: {num_list.index(7,index1+2)}")
#                             print(f">>> 007 <<< locations FIRST: {index1}, SECOND: {index1+index2+1}, THIRD: {index1+index3+2}")
            
# print("LIST 1:")
# spy_game_007(list1)
# print("LIST 2:")
# spy_game_007(list2)
# print("LIST 3:")
# spy_game_007(list3)
# print("LIST 4:")
# spy_game_007(list4)
# print("LIST 5")
# spy_game_007(list5)
# print("LIST 6")
# spy_game_007(list6)

list1 = [0,2,3,0,32,1]
list2 = [1,3,2,7,123,7,99]
list3 = [0,32,0,1,0,7]
list4 = [0,0,7]
list5 = [1,0,3,21,0,12,3,1,7]
list6 = [0,0,0,0,0,7]

def spy_game(nums):
    for index_one, item_one in enumerate(nums):
        if item_one == 0:
            print("megvan az első")
            inner_index_one = index_one + 1
            for index_two, item_two in enumerate(nums[inner_index_one:len(nums)]):
                print(item_two)
                if item_two == 0:
                    print("megvan a második")
                    print(item_two, nums.index(item_two))
                    inner_index_two = nums.index(item_two)
                    for index_three, item_three in enumerate(nums[(index_one+2):len(nums)]):
                        print(item_three)
                        if item_three == 7:
                            return True


# result = spy_game([1,2,4,0,0,7,5])
# result_print(result)

# result = spy_game([1,0,2,4,0,5,7])
# result_print(result)

# result = spy_game([1,7,2,0,4,5,0])
# result_print(result)

# result = spy_game(list1)
# result_print(result)

# result = spy_game(list2)
# result_print(result)

# result = spy_game(list3)
# result_print(result)

# result = spy_game(list4)
# result_print(result)

result = spy_game(list5)
result_print(result)

# result = spy_game(list6)
# result_print(result)
