#Do not use built-in functions except when stated otherwise! Name your functions exactly like in the
#specification

#1: Counting - DONE
"""Write a function count_a_number(numbers, number) that accepts a list of integers named
numbers and an integer named number as arguments. It counts the occurrence of the integer
number in the list and returns the count as an integer. Do not use-built-in functions! Use loops to
solve the problem."""

numbers, number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0], 2
print("Task 1: ")

def count_a_number(numbers, number):
    counter = 0
    for e in numbers:
        if number == e:
            counter += 1
    print(counter)

count_a_number(numbers, number)

print()

#Andere Versuche
#numbers_equal_to_number = [counter += 1 for number in numbers if numbers == number] - geht es auch so irgendwie?

numbers, number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0], 8
print("Task 1: ")

def count_a_number2(numbers, number):
    counter = 0
    print(len([x for x in numbers if x == number]))

count_a_number2(numbers, number)

print()


#2: Playing with lists DONE
"""Write a function play_with_lists(numbers, number) that accepts a list of integers 
named numbers and an integer named number as arguments. Use built-in list functions to achieve 
the following:
1) Print out the list in reverse order but leave the original list in order
2) Replace the given integer number within the list with the number 1 and print it on the 
console
3) Print out a sorted version of the list in descending order
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

    print("Reverse_numbers:  ", reverse_numbers[::-1]) # Task one

    if number in replaced_numbers: # Task 2 hier wird nur erste 8 ersetzt, nicht ideal - umbauen auf for
        i = replaced_numbers.index(number)
        replaced_numbers[i] = 1
        print("Replaced_numbers: ", replaced_numbers)

    replaced_numbers2 = [1 if x == number else x for x in replaced_numbers] # Task 2 mit List Comprehension, hier werden alle 8er ersetzt
    print("Replaced_numbers2:", replaced_numbers2)

    sorted_numbers1.sort(reverse = True) # Task three
    print("Sorted_numbers 1: ", sorted_numbers1)

    sorted_numbers2 = sorted(numbers, reverse = True)
    print("Sorted_numbers 2: ", sorted_numbers2)

#Unterschied zwischen sorted(list) und list.sort():
"""-
- sorted(list) --> neue Liste, originale Liste bleibt; mit jedem iterierbaren Objekt, 
- list.sort() --> ordet die originale Liste
- Hab beide erstellt, kommt drauf an was man braucht (ob Originale bestehen soll oder nicht). Hier ist es egal, da es die letzte Aufgabe ist.
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

list1, list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0], [1, 2, 3]
print("Task 3: ")
def compare_lists(list1, list2):
    print("Common elements: ", list(set(list1) & set(list2)))

compare_lists(list1, list2)
print()

# Ideen für ein anderes Mal, die noch nicht funktioniert haben:
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

items = ["Hallo", "Hallo", "Du", "Ich", 7, 8, 8, 9, 0] # nicht nur für strg funktioniert es
print("Task 4: ")
def remove_duplicates(items):
    print("Leichte Variante: ", str(list(set(items)))) #hier str bringt für den Type unten nichts
    for x in list(set(items)): #Check, ob alles eh strg ist
        print(type(x)) # hier bringt str(type(x)) auch nicht, trotzdem ints unten, hätte hier noch gern, dass alle typen in einer Liste und nicht untereinander stehen, hab es noch nicht geschafft
remove_duplicates(items) # hier teilt es mir "Hallo" z.B. wieder in einzelne Strings auf

#bei der oberen Variante hab ich items = str([ geschrieben, damit alles strg ist (aber es hat mir "Hallo" aufgeteilt, das wollte ich nicht
#lasse es jetzt so, da es für mich kein Bug sondern ein Feature ist

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0]
print("Schwere Variante: ")

def remove_duplicats_my_way(items):
    items_without_duplicates = []
    for x in items:
        if x not in items_without_duplicates:
            items_without_duplicates.append(x)
            continue
    print(items_without_duplicates)

remove_duplicats_my_way(items)

#Erste Schwache Versuche um Mitternacht:
   # items_without_duplicates = []
   #  for x in items and y in items:
   #      if (x != y):
   #          print(items_without_duplicates([x != y]))

#neue Liste wo jedes Element hinzugefügt wird, aber es macht mir jedesmal eine neue Liste....
# def remove_duplicats_my_way(items):
#     items_without_duplicates = []
#     for x in items:
#         if x not in items_without_duplicates:
#             items_without_duplicates.append(x)
#         print(items_without_duplicates)
#
# remove_duplicats_my_way(items)

#continue hinzugefügt, hier hab ich nur mehr zwei neue Liste und nicht mehr so viele - aber dennohc eine zu viel
#hab print eingerückt, nun bekomme ich nur eine korrekte Liste - finally

#5: Computer desription DONE
"""Write a function describe_computer(computer) that accepts a dictionary named 
computer as argument. The given dictionary contains the keys “Type”, “Brand” and “Price”. 
The function prints out the values of the dictionary in the following format: 
You have a TYPE from BRAND that costs PRICE€.
The capitalized words like TYPE and BRAND represent the values assigned to the keys in the 
dictionary. 
Then the function adds the key “OS” to the dictionary and defaults it to “Linux”. Afterwards it 
prints the dictionary to the console.
Example:
my_notebook = {'Type': 'Notebook', 'Brand': 'Dell', 'Price': 2000}
describe_computer(my_notebook)
Example output:
You have a Notebook from Dell that costs 2000€.
{'Type': 'Notebook', 'Brand': 'Dell', 'Price': 2000, 'OS': 'Linux'}
If one of the keys is not present, the value used in the output defaults to a custom text like “unknown 
brand” for the key “Brand”.
The function does not return anything
"""

computer = {"Type" : "Notebook", "Brand" : "Dell", "Price" : 2000, "Non" : ""}
print("Task 5: ")

def describe_computer(computer):
    type = computer.get("Type", "Notebook")
    brand = computer.get("Brand", "Dell")
    price = computer.get("Price", 2000)
    print(f"You have a {type} from {brand} that costs {price} €")

    computer.setdefault("OS", "Linux")
    print(computer)

describe_computer(computer)

#erster Schritt printen hat gepasst, es fehlt noch If one of the keys is not present, the value used in the output defaults to a text
