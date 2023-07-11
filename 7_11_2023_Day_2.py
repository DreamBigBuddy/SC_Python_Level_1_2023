# Conditionals

# Comparison operators
# ==, >, <, !=, >=, <=

# Example
num = int(input("Enter a number: "))

if num < 10:
    print("num is less than 10")

elif num > 10:
    print("num is greater than 10")

else:
    print("num is equal to 10")

# Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")

else:
    print(num, "is odd")

# Password Checker
password = "vAmAn123"

guess = input("Enter the password: ")

if guess == password:
    print("You guessed the password!")

else:
    print("Incorrect password!")

# Triangle Identifier

num = 10

if num > 10:
    print("num is larger than 10")

side_1 = int(input("Enter a side length: "))
side_2 = int(input("Enter a side length: "))
side_3 = int(input("Enter a side length: "))

if side_1 == side_2 and side_1 == side_3:
    print("Equilateral")

elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Isoceles")

else:
    print("Scalene")
