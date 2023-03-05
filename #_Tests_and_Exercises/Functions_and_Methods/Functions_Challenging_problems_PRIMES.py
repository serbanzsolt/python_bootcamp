
#? =============================================================================
#* Functions and Methods: Challenging PROBLEMS - COUNTPRIMES
#? =============================================================================

def result_print(result):
    print("The result: {}".format(result))   

def title(title):
    print("\n{}\n".format(title))
    
# ==============================================================================
#* COUNT PRIMES: Write a function that returns the *number*
#* of prime numbers that exist up to and including a given number
# ==============================================================================

def count_primes(num):
    num_list = []
    primes = []
    
    for i in range(0,num+1):
        num_list.append(i)
    # print(f"The list is : {num_list}")
    for number in range(2, num_list[-1]+1):
        divider_counter = 0
        for divider in range(1, number):
            # print(f"{number} % {divider} = {number % divider}")
            if number % divider == 0:
                divider_counter += 1
                if divider_counter > 1:
                    break
            # print(f"Divider_counter: {divider_counter}")
        if divider_counter == 1:
            primes.append(number)
            # print(f"FOUND A PRIME!: {number}")
    return primes
        
result = count_primes(100)
result_print(result)