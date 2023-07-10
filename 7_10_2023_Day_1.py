# This is a comment
# Can be used to make notes in your program

# Print Statement
print("Hello World") # "Hello World"

# Print Statement with sep and end parameters
print("Hello", "World", sep="&", end="!") # "Hello&World!"

# Creates an integer
my_int = 1

# Creates a string
my_str = "Hello"

# Prints out values
print(my_int)
print(my_str)

# Getting user input and printing it
name = input("Enter your name: ") # Gets user's name
print("Hello", name) # Greets the user with name

# Different formatting types for print statements
print("Hello " + name)
print("Hello", name)
print(f"Hello {name}")
print("Hello {0}".format(name))

# Number input from the user
my_input = int(input("Enter a number: ")) # Gets a number from the user
my_input2 = int(input("Enter another number: "))
print(my_input + my_input2)

my_input = int(input("Enter another number: "))
print(my_input + 10) # Adds the number from the user to 10

my_int = 1

my_int2 = my_int * 2
print(my_int2)
