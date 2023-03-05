
#? =============================================================================
#* Homework - Errors and Exceptions: Problem 3
#? =============================================================================

def ask():
    while True:
        try:
            result = int(input("Please provide an integer: "))
        except:
            print("This was not an integer! Try Again!")
            continue
        else:
            print(f"The given number was: {result} and it's squared: {result ** 2}")
            break
ask()