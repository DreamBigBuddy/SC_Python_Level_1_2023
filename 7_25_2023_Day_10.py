# Max of 3 Numbers
def max_of_3(num, num2, num3):
    if num > num2 and num > num3:
        return num

    elif num2 > num and num2 > num3:
        return num2

    else:
        return num3

num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

print(max_of_3(num, num2, num3))

# Time, Math, and Random Modules
import time, math, random, turtle

print("Before")
time.sleep(1) # Pauses program for 1 second
print("After")

print(math.ceil(100/9)) # Rounds up to nearest whole number
print(math.floor(100/9)) # Rounds down to nearest whole number

print(random.randint(1, 100)) # Picks a random number in 1-100 range

# Turtle Functions
t.forward(100)
t.backward(100)
t.right(90)
t.left(90)

# Draw Shape with Any Number of Sides
sides = int(input("Enter number of sides: "))
side_length = int(input("Enter a side length: "))

t = turtle.Turtle()

for i in range(sides):
    t.forward(side_length)
    t.right(360/sides)

# Other Turtle Functions
t = turtle.Turtle()

t.speed(0)

t.pensize(10)

t.color("blue")
t.fillcolor("green")

t.begin_fill()
t.circle(50, 360, 3)
t.end_fill()

t.penup()
t.goto(100, 100)
t.pendown()

t.forward(100)

t = turtle.Turtle()

# Draw shapes at random location forever
ans = ""

while ans == "":
    sides = int(input("Enter number of sides: "))
    side_length = int(input("Enter a side length: "))

    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()

    for i in range(sides):
        t.forward(side_length)
        t.right(360/sides)

    ans = input("Press enter to go again: ")

# Draw Smiley Face
t = turtle.Turtle()

t.speed(0)

t.begin_fill()
t.color("yellow")
t.circle(100)
t.end_fill()

t.pu()
t.goto(-35, 125)
t.pd()

t.color("black")

t.begin_fill()
t.circle(20)
t.end_fill()

t.pu()
t.goto(35, 125)
t.pd()

t.begin_fill()
t.circle(20)
t.end_fill()

t.pu()
t.goto(-50, 75)
t.pd()

t.pensize(10)

t.rt(90)

t.circle(50, 180)
