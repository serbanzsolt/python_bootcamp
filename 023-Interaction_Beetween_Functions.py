
#? =============================================================================
#* 023 - Interactions between functions
#? =============================================================================

example = [1,2,3,4,5,6,7]
from random import shuffle

#shuffle(example)
#print(example)

print(f"Example list: {example}")
result = shuffle(example)
print (f"Shuffle function not returning any value: {result} \nNeed to create an own one")

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(f"After used the created function: {result}")

# ==============================================================================
#* Guessing game
# ==============================================================================

gamelist = [" ", "O", " "]

def player_guess():
    guess =""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2: ")
        
    return int(guess)

myindex = player_guess()
print(f"The player's guess is: {myindex}")

def check_guess (mylist, guess):
    if mylist[guess] == "O":
        print("Correct!")
        print(mylist)
    else:
        print("Wrong guess!")
        print(mylist)
        
# INITIAL LIST
mylist = [" ", "O", " "]
# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)
# USER GUESS
guess = player_guess()
# CHECK GUESS
check_guess(mixedup_list, guess)