import random

def random_power():
    def f(x):
        return x**2
    def g(x):
        return x**3
    def h(x):
        return x**4
    
    functions = [f,g,h]
    return random.choice(functions)

for i in range(10):
    p = random_power()
    print(p(10))

print("-------------------------------------------------------------")

