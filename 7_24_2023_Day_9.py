# Day 9

# Assignment from Day 8: Interactive List
my_list = []

option = ""

while option != "exit":
    option = input("Enter an option (show, add, remove, replace): ").lower()

    if option == "show":
        print(f"Here are the contents of your list: {my_list}")

    elif option == "add":
        values = input("Enter the values to add: ").replace(" ", "").split(",")
        my_list.extend(values)
        print(f"Here are the contents of your list: {my_list}")

    elif option == "remove":
        choice = input("Remove by value or index? ").replace(" ", "").lower()
        if choice == "value":
            value = input("Enter the value to remove: ")
            while my_list.count(value) > 0:
                my_list.remove(value)
            
            print(f"Here are the contents of your list: {my_list}")

        elif choice == "index":
            index = int(input("Enter the index: "))-1
            if index <= len(my_list) and index > 0:
                my_list.pop(index)
                print(f"Here are the contents of your list: {my_list}")

            else:
                print("Please enter an index within 1 and the length of the list")

    elif option == "replace":
        choice = input("Remove by value or index? ").replace(" ", "").lower()
        if choice == "value":
            old_value = input("Enter the value to replace with: ")
            new_value = input("Enter the value to replace the old value: ")
            for i in range(len(my_list)):
                if my_list[i] == old_value:
                    my_list[i] = new_value

        elif choice == "index":
            index = int(input("Enter the index to replace: "))-1
            value = input("Enter the value to replace with: ")
            my_list[index] = value

        print(f"Here are the contents of your list: {my_list}")

# Prime Number Checker
def check_if_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False

    return True

print(check_if_prime(37))

# Factorial Calculator
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i

    return total

print(factorial(0))
