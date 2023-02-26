def play_again():
    correct_aswer = True
    while correct_aswer == True:
        user_choice = input("Play AGAIN?... Y/N: ")
        if user_choice.lower() == "y":
            print("előtte")
            correct_aswer == False
            print("utána")
            return True
        elif user_choice.lower() == "n":
            correct_aswer == False
            return False
        else:
            print("Wrong input! Use 'Y' or 'N'...")
            
x = play_again()

