
#? =============================================================================
#* Functions and Methods: LEVEL 1 PROBLEMS
#? =============================================================================

def result_print(result):
    print("The result: {}".format(result))   

def title(title):
    print("\n{}\n".format(title))
    
# ==============================================================================
#* OLD MACDONALD: Write a function that capitalizes the first and fourth letters
#* of a name 
# ==============================================================================

def old_macdonald(name):
    name = name.lower()
    return_name = ""
    for i in range(0, len(name)):
        if (i == 0) or (i == 3) :
            return_name += name[i].upper()
        else:
            return_name += name[i]
    return return_name

result = old_macdonald("macdonald")
result_print(result)

result = old_macdonald("MACDONALD")
result_print(result)

result = old_macdonald("mACdONALD")
result_print(result)

# ==============================================================================
#* MASTER YODA: Given a sentence, return a sentence with the words reversed
# ==============================================================================

def master_yoda(text):
    list_of_words = text.split(" ")
    list_of_words = list_of_words[::-1]
    return_text = ""
    for word in list_of_words:
        return_text += (word + " ")
    return_text = return_text[0:(len(return_text)-1)]
    print(return_text)
    
master_yoda("I am home")
master_yoda("We are ready")

# ==============================================================================
#* MASTER YODA2 - Using join() stringmethod
# ==============================================================================

def master_yoda2 (text):
    words_in_list = text.split()
    print( " ".join(words_in_list[::-1]) ) 

master_yoda2("I am home")
master_yoda2("We are ready")

# ==============================================================================
#* ALMOST THERE: Given an integer n,
#* return True if n is within 10 of either 100 or 200
# ==============================================================================

def almost_there(n):
    n = abs(n)
    if (n >= 90 and n <= 110) or (n >= 190 and n <= 210):
        return True
    else:
        return False
    
result = almost_there(104)
result_print(result)

result = almost_there(150)
result_print(result)

result = almost_there(209)
result_print(result)