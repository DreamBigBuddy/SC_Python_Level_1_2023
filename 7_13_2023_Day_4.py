# Day 4

# Continue Example
for i in range(10):
    if i == 5:
        continue

    print(i)

'''
Returns:
0
1
2
3
4
6
7
8
9
'''

# Break Example
for i in range(10):
    if i == 5:
        break

'''
Returns:
0
1
2
3
4
'''

# Guessing Game

import random

num = random.randint(1, 100)

guess = int(input("Take a guess: "))

while guess != num:
    print("Incorrect!")
    guess = int(input("Take a guess: "))

print("Correct!")
