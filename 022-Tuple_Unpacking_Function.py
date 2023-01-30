
#? =============================================================================
#* 022 - Tuple unpacking with fuctions
#? =============================================================================

stock_prizes = [
    ('Apple',200),
    ("Google", 400),
    ("Mcrosoft", 100)
]

for item in stock_prizes:
    print(item)
    
#* TUPLE Unpacking

for ticker, price in stock_prizes:
    print(ticker)
    print(price)
    
print("Ten percent increase in prices: ")
for ticker, price in stock_prizes:
    print(ticker, " - ", (price + 0.1 *price) )
    
#* work hours example

work_hours = [
    ("Abby", 100),
    ("Billy",400),
    ("Cassy",800)
]

def employee_check (work_hours):
    current_max = 0
    employee_of_month = ""
    
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # RETURN
    return (employee_of_month, current_max)

print(f"Who worked the most hours: {(employee_check(work_hours))}")

result = employee_check(work_hours)
name,hours = result
print(name)