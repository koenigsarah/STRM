#Do not use built-in functions except when stated otherwise! Name your functions exactly like in the
#specification

#1: Counting - DONE
"""Write a function count_a_number(numbers, number) that accepts a list of integers named
numbers and an integer named number as arguments. It counts the occurrence of the integer
number in the list and returns the count as an integer. Do not use-built-in functions! Use loops to
solve the problem."""

numbers, number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0], 8
print("Task 1: ")

def count_a_number(numbers, number):
    counter = 0
    for e in numbers:
        if number == e:
            counter += 1
    print(counter)

count_a_number(numbers, number)

print()

#Verbesserungen für ein anderes Mal:
#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0]
#numbers_equal_to_number = [number.count() for e in numbers if number == e]


#2: Playing with lists DONE
"""Write a function play_with_lists(numbers, number) that accepts a list of integers 
named numbers and an integer named number as arguments. Use built-in list functions to achieve 
the following:
 Print out the list in reverse order but leave the original list in order
 Replace the given integer number within the list with the number 1 and print it on the 
console
 Print out a sorted version of the list in descending order
Don’t forget that lists are mutable. You probably will have to make a copy if you want the leave the 
original list untouched. Investigate the difference between using the build-in function 
sorted(list) and the sort function of the class list. Write a comment why you chose the 
sorting function you used.
The function does not return anything."""

numbers, number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0], 8
print("Task 2: ")
def play_with_lists(numbers, number):
    reverse_numbers = numbers
    replaced_numbers = numbers
    sorted_numbers1 = numbers

    print("Reverse_numbers: ", reverse_numbers[::-1]) # Task one

    if number in replaced_numbers:
        i = replaced_numbers.index(number)
        replaced_numbers[i] = 1
        print("Replaced_numbers: ", replaced_numbers)

    sorted_numbers1.sort(reverse = True) # Task three
    print("Sorted_numbers 1: ", sorted_numbers1)

    sorted_numbers2 = sorted(numbers, reverse = True)
    print("Sorted_numbers 2: ", sorted_numbers2)

#Unterschied zwischen sorted(list) und list.sort():
"""-
- sorted(list) --> neue Liste, originale Liste bleibt; mit jedem iterierbaren Objekt, 
- list.sort() --> ordet die originale Liste
- Habe eine neue Variable erstellt und .sort() genommen, damit die Originale bestehen bleibt - sorted_numbers und reverse_numbers passt für mich so besser zusammen
"""

play_with_lists(numbers, number)
print()

#Verbesserungen für später

    # numbers_ersetzen = [1 if number == numbers_ersetzen else number for number in numbers_ersetzen] # Task two
    # print(numbers_ersetzen)
     # for i, number in enumerate(numbers_ersetzen): # Task two
    #     if number == numbers_ersetzen:
    #         numbers_ersetzen[i] == 1
    #     print(numbers_ersetzen)

    # numbers_ersetzen = [1 if number == numbers_ersetzen else number for number in numbers_ersetzen] # Task two
    # print(numbers_ersetzen)


#for e in reversed(numbers): #Task one - does not modify the list, just get a view, but not a list
       #print(e)
#print(reverse_numbers.reverse())


#3: Comparing list elements DONE
"""Write a function compare_lists(list1, list2) that accepts two list as arguments. The
function looks for elements that the two lists have in common. It returns a list containing all those 
elements. This list may be empty if there are no common elements"""

list1, list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0], [1,2,3]
print("Task 3: ")
def compare_lists(list1, list2):
    print("Common elements: ", list(set(list1) & set(list2)))

compare_lists(list1, list2)
print()

# Ideen für ein anderes Mal:
# list3 = []
#     for x in list1:
#         for y in list2:
#             if (x == y):
#                 print(list([x]))

#4: No duplicates!
"""Write a function remove_duplicates(items) that accepts a list of strings named items as 
argument and removes all duplicate values from the list. There is an easy way to do this using 
another container. Search for this way and implement it. 
Then write another function named remove_duplicates_my_way(items). This time find a 
way to accomplish the task without using another container.
Both functions return the list of strings without duplicates."""

items = ["Hallo", "Hallo", "Du", "Ich", 7, 8, 8, 9, 0] # geht mit Zahlen auch
print("Task 4: ")
def remove_duplicates(items):
    print("Leichte Variante: ", list(set(items)))
remove_duplicates(items)


items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0]

def remove_duplicats_my_way(items):
    print()

remove_duplicats_my_way(items)


#5: Computer desription DONE
"""Write a function describe_computer(computer) that accepts a dictionary named 
computer as argument. The given dictionary contains the keys “Type”, “Brand” and “Price”. 
The function prints out the values of the dictionary in the following format"""

computer = {"Type" : "Notebook", "Brand" : "Dell", "Price" : 2000}
print("Task 5: ")

def describe_computer(computer):
    type = computer.get("Type", "Notebook")
    brand = computer.get("Brand", "Dell")
    price = computer.get("Price", 2000)
    print(f"You have a {type} from {brand} that costs {price} €")

    computer.setdefault("OS", "Linux")
    print(computer)

describe_computer(computer)
