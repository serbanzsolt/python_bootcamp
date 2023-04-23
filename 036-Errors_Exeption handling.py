
#? =============================================================================
#* 034 - Error and Exeptions
#? =============================================================================

"""
try: - This is the block of code to be attemted(may lead to an error)
except: - Block of code that will execute in case of there is an error
finally: - A final block of code that will be executed regardless of an error
"""

def add (number1, number2):
    print(number1+number2)
    
add(10,20)

number1 = 10
# number2 = input("Please provide a number: ")

#*Generate error
# add(number1, number2)
print("Something happened") #*this wont run if error happened

# ==============================================================================
#* TRY, EXCEPT, ELSE
# ==============================================================================

try:
    #Want to attempt this code. May have an error
    result = 10 + 5
except:
    print("It looks like you aren't adding correctly!")
else:
    print("Add went well")
    print(result)
    
# ==============================================================================
#* TRY, EXCEPT? FINALLY
# ==============================================================================
print("\nWriting into a file:")

try:
    f = open("testfile", "w") # r generate OS error
    f.write("Write test in the file")
    f.close()
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey, you have an OS error!")
except:
    print("All other exceptions")
finally:
    print("I always run")
    
def ask_for_int():
    while True:
        try:
            result = int(input("Please provde number: "))
        except:
            print("Whoops! Thats not a number")
            continue
        else:
            print("Yes thank you!")
            break
        # finally:
        #     print("End of Try / Except / Finally")
        
ask_for_int()