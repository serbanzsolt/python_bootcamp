
#? =============================================================================
#* Functions and Methods: Challenging PROBLEMS - PRINTBIG
#? =============================================================================

one_star = [
            "*    ", #0
            " *   ", #1
            "  *  ", #2
            "   * ", #3
            "    *"  #4
            ]

two_star = [
            "**   ", #0
            " **  ", #1
            "  ** ", #2
            "   **", #3
            "* *  ", #4
            "*  * ", #5
            "*   *", #6
            " * * ", #7
            " *  *", #8
            "  * *"  #9
            ]

three_star = [
            "***  ", #0
            " *** ", #1
            "  ***", #2
            "* ** ", #3
            "*  **", #4
            " * **", #5
            "** * ", #6
            "**  *"  #7
            ]

four_star = [
            "**** ", #0
            " ****", #1
            "* ***", #2
            "** **", #3
            "*** *"  #4
            ]

five_star = [
            "*****" #0
            ]

letter_A = {
    "line_1" : one_star[2],
    "line_2" : two_star[7],
    "line_3" : five_star[0],
    "line_4" : two_star[6],
    "line_5" : two_star[6]
    }

letter_B = {
    "line_1" : four_star[0],
    "line_2" : two_star[6],
    "line_3" : four_star[0],
    "line_4" : two_star[6],
    "line_5" : four_star[0]
    }

letter_C = {
    "line_1" : five_star[0],
    "line_2" : one_star[0],
    "line_3" : one_star[0],
    "line_4" : one_star[0],
    "line_5" : five_star[0]
    }

letter_D = {
    "line_1" : four_star[0],
    "line_2" : two_star[6],
    "line_3" : two_star[6],
    "line_4" : two_star[6],
    "line_5" : four_star[0]
    }

letter_E = {
    "line_1" : five_star[0],
    "line_2" : one_star[0],
    "line_3" : five_star[0],
    "line_4" : one_star[0],
    "line_5" : five_star[0]
    }

letters = {
            "a" : letter_A,
            "b" : letter_B,
            "c" : letter_C,
            "d" : letter_D,
            "e" : letter_E
}

# def print_letter (letter):
#     for line in letter.value():
#         print(line)
#     print("")

# print_letter(letter_A)

for line in letter_A.values():
    print(line)
print("")
for line in letter_B.values():
    print(line)
print("")
for line in letter_C.values():
    print(line)
print("")
for line in letter_D.values():
    print(line)
print("")
for line in letter_E.values():
    print(line)
print("")