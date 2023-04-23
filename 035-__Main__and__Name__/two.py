import one

print("Top level in two.py")

one.FUNC()

if __name__ == "__main__":
    print("two.py is being run direcly")
else:
    print("two.py has been imported")