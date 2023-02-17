
#? =============================================================================
#* Functions and Methods Homework
#? =============================================================================

# ==============================================================================
#* Write a function that computes the volume of a sphere given its radius
#* The volume of a sphere is given as $$\frac{4}{3} πr^3$$
# ==============================================================================
import math

def vol(rad):
    return (4/3) * math.pi * rad**3

print(vol(25))
print(vol(2))

# ==============================================================================
#* Write a function that checks whether a number is in a given range (inclusive of high and low)
# ==============================================================================

def ran_check(num,low,high):
    if num >= low and num <= high:
        return print(f"{num} is in the range of {low} and {high}")
    else:
        return print(f"{num} is not in the range of {low} and {high}")

ran_check(5, 2, 7)
ran_check(3, 1, 10)
ran_check(10, 1, 3)

def check(num, low, high):
    return num in range(low, high+1)

print(check(5, 2, 7))
print(check(3, 1, 10))
print(check(10, 1, 3))

# ==============================================================================
#* Write your Comment here!Write a Python function that accepts a string 
#* and calculates the number of upper case letters and lower case letters
# ==============================================================================

def up_low(s):
    upper_counter = 0
    lower_counter = 0
    print(s)
    for i in range(0, len(s)):
        if s[i].isupper():
            upper_counter += 1
        elif s[i].islower():
            lower_counter += 1
        else:
            pass
    return print(f"Number of upper characters: {upper_counter}\nNumber of lower characters: {lower_counter}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# ==============================================================================
#* Write a Python function that takes a list and returns a new list with unique elements of the first list.
# ==============================================================================

def unique_list(lst):
    return list(set(lst))

newlist = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(newlist)

# ==============================================================================
#* Write a Python function to multiply all the numbers in a list.
# ==============================================================================

def multiply(numbers):
    sum = 1
    for i in numbers:
        sum *= i
    return sum
print(multiply([1,2,3,-4]))

# ==============================================================================
#* Write a Python function that checks whether a word or phrase is palindrome or not.
#* Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
#* e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the
#* .replace() method in a string to help out with dealing with spaces.
#* Also google search how to reverse a string in Python, there are some clever ways 
#* to do it with slicing notation.
# ==============================================================================

def palindrome(s):
    # s = s.replace(" ","")
    s = s.split()
    s = "".join(i.lower() for i in s)
    return ( s == s[::-1] )

print(palindrome("madam"))
print(palindrome("island"))
print(palindrome("mAdam"))
print(palindrome("NursEs rUn"))

# ==============================================================================
#* Write a Python function to check whether a string is pangram or not.
#* (Assume the string passed in does not have any punctuation)
#*  Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#*    For example : "The quick brown fox jumps over the lazy dog"
#* Hint: You may want to use .replace() method to get rid of spaces.
#* Hint: Look at the [string module](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)
#* Hint: In case you want to use [set comparisons](https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41)
# ==============================================================================

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.split()
    str1 = "".join ([word for word in str1])
    str1 = str1.lower()
    str1 = list(set(str1))
    str1.sort()
    str1 = "".join ([letter for letter in str1])
    print(str1)
    print(alphabet)
    if str1 == alphabet:
        return True
    else:
        return False


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The quick brown fox jumps the lazy dog"))
print(ispangram("Sphinx of black quartz judge my vow"))
print(ispangram("The five boxing wizards jump quickly"))