# Day 3

# For Loops
# Range Function will always end one less than the stop
for i in range(0, 10, 2): # Range Structure: (start, stop, step)
    print(i)

'''
Returns:
0
2
4
6
8
'''

# For Loop Example
messages = ""

num_of_messages = int(input("Enter how many messages: "))

for i in range(num_of_messages):
    message = input("Enter your message: ")

    messages += message + "\n"

print(messages)

###########################################

# While Loops
i = 0

while i < 10:
    print(i)
    i += 1

'''
Returns:
0
1
2
3
4
5
6
7
8
9
'''

# While Loop Example
messages = ""

message = input("Enter a message: ")

while message != "done":
    messages += message + "\n"
    message = input("Enter a message: ")

print(messages)

###########################################

# Pyramid Maker
length = int(input("Enter length of pyramid: "))
for i in range(length):
    print("#" * (i+1))

'''
Sample Output if length equaled 5:
#
##
###
####
#####
'''
###########################################

# Add Up Numbers (For Loop)
nums = int(input("Enter how many numbers: "))
total = 0

for i in range(nums):
   num = int(input("Enter a number: "))
   total += num
   
print("your total is", total)

###########################################

# Add Up Numbers (While Loop)

total = 0

num = int(input("Enter a number: "))

while num > 0:
    total += num

    num = int(input("Enter a number: "))

print(total)
