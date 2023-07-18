# Odd Remover (With Two Loops)
numbers = []

num = int(input("Enter a number: "))

while num > 0:
    numbers.append(num)
    num = int(input("Enter a number: "))
  
even_list = []

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)

print(even_list)

# Odd Remover (With One Loop)
numbers = []

num = int(input("Enter a number: "))

while num > 0:
    if num % 2 == 0:
        numbers.append(num)

    num = int(input("Enter a number: "))

print(numbers)

even_list = []

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)

print(even_list)

# Summing All Numbers from User Input
numbers = input("Enter some numbers: ").split(", ")
total = 0
for i in range(len(numbers)):
    total += int(i)

print(total)

# Multiple Finder v2
numbers = input("Enter some numbers: ").split(", ")
factor = int(input("Enter another number: "))
multiples_list = []

for i in numbers:
    if int(i) % factor == 0:
        multiples_list.append(int(i))

print(multiples_list)

# Grade Calculator
grades = input("Enter some grades: ").split(", ")
total = 0

for i in grades:
    total += int(i)

avg = total / len(grades)

if avg >= 90 and avg <= 100:
    print("Your Letter Grade is an A")
                
elif avg >= 80 and avg < 90:
    print("Your Letter Grade is a B")
    
elif avg >= 70 and avg < 80:
    print("Your Letter Grade is a C")
    
elif avg >= 60 and avg < 70:
    print("Your Letter Grade is a D")
    
elif avg >= 0 and avg < 60:
    print("Your Letter Grade is an F")
