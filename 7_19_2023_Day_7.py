################################ STRINGS ##############################
my_str = "aHello Worlda"
'''
.find
.count
.split
.replace
.strip
.isupper
.islower
'''

print(my_str.find("o")) # 5

print(my_str.find("z")) # -1 because it is not in string

print(my_str.count("l")) # 3

print(my_str.count("z")) # 0 because it is not in string

print(my_str.split(" ")) # ["aHello", "Worlda"]

print(list(my_str)) # ['a', 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', 'a'] because the list function will split up the string by its characters

print(my_str.replace("l", "a")) # 'aHeaao Worada'

print(my_str.strip("a")) # "Hello World" because it removes stuff in the beginning and end of string

for i in my_str:
    print(i, i.isupper(), i.islower())

# Returns
'''
a False True
H True False
e False True
l False True
l False True
o False True
  False False
W True False
o False True
r False True
l False True
d False True
a False True
'''

print(my_str[2:]) # 'llo World' Starts at index 2 to end

print(my_str[2:8]) # 'llo Wo' Starts at index 2 and ends at index 8

print(my_str[2:8:2]) # 'loW' Starts at index 2 and ends at index 8, going by 2 indexes

############################### LISTS ################################

my_list = [4, 1, 5, 5, 11, 9, 10]
'''
.append
.remove
.insert
.pop
.sort
.reverse
.count
.index
.extend
'''
my_list2 = [2, 4, 9, 7, 9]

my_list.append(2)
print(my_list) # [4, 1, 5, 5, 11, 9, 10, 2]

my_list.remove(2)
print(my_list) # [4, 1, 5, 5, 11, 9, 10]

my_list.insert(1, 2)
print(my_list) # [4, 2, 1, 5, 5, 11, 9, 10]

my_list.pop(1)
print(my_list) # [4, 1, 5, 5, 11, 9, 10]

my_list.sort()
print(my_list) # [1, 4, 5, 5, 9, 10, 11]

my_list.reverse()
print(my_list) # [11, 10, 9, 5, 5, 4, 1] Based on the .sort() because .sort() modified the list. Reverse will just flip the order of the list

print(my_list.count(5)) # 2

print(my_list.index(11)) # 4
print(my_list.index(5)) # 2 because it only gives first occurrence
print(my_list.index(100)) # Errors because 100 not in list

my_list.extend(my_list2)
print(my_list) # [4, 1, 5, 5, 11, 9, 10, 2, 4, 9, 7, 9]

print(my_list[4:]) # [11, 9, 10, 2, 4, 9, 7, 9] Starts at index 4 to end

print(my_list[4:10]) # [11, 9, 10, 2, 4, 9] Starts at index 4 and ends at index 10

print(my_list[4:10:2]) # [11, 10, 4] Starts at index 4 and ends at 10, going by 2 indexes

############################## PART 1 LIST EXERCISE ################################
# Add an item
# my_list.append(item)

# Remove an item
# my_list.remove(item)

# Replace an item
# my_list[index] = value

my_list = []

option = ""

while option != "exit":
    option = input("Enter an option (show, add, remove, replace): ").lower()

    if option == "show":
        print(f"Here are the contents of your list: {my_list}")

    elif option == "add":
        value = input("Enter the value to add: ")
        my_list.append(value)
        print(f"Here are the contents of your list: {my_list}")

    elif option == "remove":
        value = input("Enter the value to remove: ")
        my_list.remove(value)
        print(f"Here are the contents of your list: {my_list}")

    elif option == "replace":
        index = int(input("Enter the index to replace: "))-1
        value = input("Enter the value to replace with: ")
        my_list[index] = value
        print(f"Here are the contents of your list: {my_list}")

############ UPPERCASE AND LOWERCASE COUNTER ##############
my_string = str(input("Give a string: "))
upper = []
lower = []
for i in my_string:
    if i.isupper():
        upper.append(i)

    if i.islower():
        lower.append(i)

print("Uppercase:", upper)
print("Lowercase:", lower)
