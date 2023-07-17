# Lists
my_list = ["e", "a", "c", "b", "d"]

# List Methods
my_list.append("f")
print(my_list)

my_list.remove("f")
print(my_list)

my_list.insert(1, "f")
print(my_list)

my_list.pop(1)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

# Lists in Loops
for i in my_list: # Don't do this if you are modifying (adding/removing values) the list
    if i == "c":
        i = 1

for i in range(len(my_list)): # Do this
    if my_list[i] == "c":
        my_list[i] = 1

print(my_list)

# Multiple Finder

multiple = int(input("Enter a number to find multiples of: "))
max_num = int(input("Enter a max number: "))

multiples = []

for i in range(1, max_num+1):
    if i % multiple == 0:
        multiples.append(i)

print("Here are your multiples: {0}".format(multiples))
