# Day 8

# Replace Function

string = input("Enter a phrase: ")
char = input("Enter a character to remove: ")

while string.find(char) != -1:
    index = string.find(char)

    string = string[:index] + string[index+len(char):]

print(string)

# Function Structure
'''
def <name>(params):
    code
'''

# Simple print function with parameter
def print_name(name):
    print(f"Hi {name}!")

print_name("John")

# Add function

def add(x, y):
    print(x+y)

add(1, 2)

# Replace function with default arguments
def replace(string, substr, replace_str=""):
    while string.find(substr) != -1:
        index = string.find(substr)

        string = string[:index] + replace_str + string[index+len(substr):]

    return string

string = input("Enter a phrase: ")
substr = input("Enter a character to remove: ")
replace_str = input("Enter a replace value: ")

replaced_string = replace(string, substr, replace_str)
print(f"Your replaced string: {replaced_string}")

# Any length argument values
def values(*args):
    return args

data = values(1, 2, 3, 4)
print(data) # (1, 2, 3, 4)

# Keyword arguments
def values(**kwargs):
    return kwargs

data = values(first_name="Vaman", last_name="Rajagopal")
print(data) # {'first_name': 'Vaman', 'last_name': 'Rajagopal'}

# Reverse String
def reverse_string(string):
    return string[::-1]

string = input("Enter a string: ")

print(f"Here is your reversed string: {reverse_string(string)}")

# Palindrome Checker
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string)-1

    while right_pos >= left_pos:
        if string[left_pos] != string[right_pos]:
            return False

        left_pos += 1
        right_pos -= 1

    return True

print(isPalindrome("racecar"))
print(isPalindrome("Vaman"))
