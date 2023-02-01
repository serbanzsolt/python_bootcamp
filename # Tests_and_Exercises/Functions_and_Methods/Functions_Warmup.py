
#? =============================================================================
#* Functions and Methods: WARMUP
#? =============================================================================

def result_print(result):
    print("The result: {}".format(result))   

def title(title):
    print("\n{}\n".format(title))

# ==============================================================================
#* LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even,
# *but returns the greater if one or both numbers are odd
# ==============================================================================
title("LESSER OF TWO EVENS")

def lesser_of_two_evens(a,b):
    if (a % 2 and b % 2) == 0 :
        if a > b:
            return b
        elif a < b:
            return a
        else:
            print("The given even numbers are equal")
    elif (a % 2 and b % 2) == 1 :
        if a > b:
            return a
        elif a < b:
            return b
        else:
            print("The given odd numbers are equal")
    else:
        print("the given numbers are odd and even")
        
result = lesser_of_two_evens(11, 23)
result_print(result)

result = lesser_of_two_evens(11, 11)
result_print(result)

result = lesser_of_two_evens(16, 22)
result_print(result)

result = lesser_of_two_evens(16, 16)
result_print(result)

result = lesser_of_two_evens(0, 0)
result_print(result)

# ==============================================================================
#* ANIMAL CRACKERS: Write a function takes a two-word string
#* and returns True if both words begin with same letter
# ==============================================================================

title("ANIMAL CRACKERS")

def animal_crackers(text):
    text = text.lower()
    list_of_words = text.split(" ")
    if len(list_of_words) == 2:
        if list_of_words[0][0] == list_of_words[1][0]:
            return True
        else:
            return False
    else:
        print("You need to give a two word string!")
        
result = animal_crackers("Levelheaded Llama")
result_print(result)

result = animal_crackers("Crazy Kangoroo")
result_print(result)

result = animal_crackers("Two many words given")
result_print(result)

# ==============================================================================
#* MAKES TWENTY: Given two integers, 
#* return True if the sum of the integers is 20 
#* *or* if one of the integers is 20. If not, return False
# ==============================================================================

title("MAKES TWENTY")

def makes_twenty(a,b):
    if (a + b) == 20:
        return True
    elif (a == 20) or (b == 20):
        return True
    else:
        return False
    
result = makes_twenty(20, 10)
result_print(result)

result = makes_twenty(12, 8)
result_print(result)

result = makes_twenty(2, 3)
result_print(result)