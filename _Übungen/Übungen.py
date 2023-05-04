# # # 1: famous quote
# #
# # quote = '"Even I don´t wake up looking like Cindy Crawford"'
# # author = "Cindy Crawford"
# # print(author, "once said", quote)
# # #Result: Cindy Crawford once said "Even I don´t wake up looking like Cindy Crawford"
#
# # 2: number eight
#
# # def number_eight()
# #     print(5+3)
# #     print(5+3)
# #     print(5+3)
# #     print(5+3)
# #     print(5+3)
#
# # 3: formatting
#
# #Lists
# l = []
#
# # # Adding Element into list
# # l.append(5)
# # l.append(10)
# # print("Adding 5 and 10 in list", l)
# #
# # # Popping Elements from list
# # l.pop()
# # print("Popped one element from list", l)
# # print()
# #
# # Set
# s = set()
#
# # Adding element into set
# s.add(5)
# s.add(10)
# print("Adding 5 and 10 in set", "Länge", len(s))
#
# print(s.discard(5))
#
#
# # # Removing element from set
# # s.remove(5)
# # print("Removing 5 from set", s)
# # print()
# #
# # # Tuple
# # t = tuple(l)
# #
# # # Tuples are immutable
# # print("Tuple", t)
# # print()
#
# # Dictionary
# d = {}
#
# # # Adding the key value pair
# # d[5] = "Five"
# # d[10] = "Ten"
# # print("Dictionary", len(d))
# #
# # print(d[5])
# #
# # # Removing key-value pair
# # del d[10]
# # print("Dictionary", d)


# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])
#
# print()

# def name_age():
#     name = input("Please enter your name: ")
#     age = int(input("Please enter your age: "))
#
#     # Method 1: Concatenation
#     print("Hello, " + name + ". You are " + str(age) + " years old.")
#
#     # Method 2: String format()
#     print("Hello, {}. You are {} years old.".format(name, age))
#
#     # Method 3: f-strings
#     print(f"Hello, {name}. You are {age} years old.")
# name_age()

# def f(name, n):
#     print("Hello", name)
#     if (n > 0):
#             f(name + 1, n-1)
# f("s", 3)

# street, housenumber = input("Sag mir bitte zuerst eine Straße unter 5 Zeichen und dann eine Hausnummer: ").split()
#
# def street_housenumber (street, housenumber):
#     if len(street) < 6:
#         print("Das ist zu kurz")
#         continue
#     try:
#         housenumber = int(housenumber)
#     except ValueError:
#         print("Es muss eine ganze Zahl sein")
#         continue
#     else:
#         print(street, housenumber)
#         break
#
# street_housenumber(street, housenumber)
# #
# #
#

#
# def get_user_input():
#     while True:
#         try:
#             str_input = input("Geben Sie eine Zeichenkette mit mindestens 5 Zeichen ein: ")
#             if len(str_input) < 5:
#                 raise ValueError("Die eingegebene Zeichenkette ist zu kurz.")
#             break
#         except ValueError as err:
#             print(err)
#
#     while True:
#         try:
#             num_input = int(input("Geben Sie eine ganze Zahl ein: "))
#             break
#         except ValueError:
#             print("Die Eingabe ist nicht numerisch.")
#
#     print("Sie haben folgende Werte eingegeben: Zeichenkette = {}, Zahl = {}".format(str_input, num_input))
#
# get_user_input()

# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
#
# def sum_iterative(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     print(result)
#
# sum_iterative(numbers)
#
# def sum_rekursiv(numbers):
#     if not numbers:
#         return 0
#     else:
#         return numbers[0] + sum_rekursiv(numbers[1:])
#
# print(sum_rekursiv([1, 2, 3, 4, 5]))
#
# def exponentiate(base, exponent):
#     result = 1
#     for i in range(exponent):
#         result *= base
#     return result
#
# exponentiate(base, exponent)

# list = [3, "Hallo", 3.5, 4j]
# newlist = [x for x in list if type(x) == complex]
# print(newlist)
#
#
# n = 0
#
# def is_prime(n):
#     if n <2:
#         return False
#     for i in range(2, int(n ** 0.5) +1):
#         if n % i == 0:
#             return False
#     return True
#
# start, end = 1, 100
# primes = [num for num in range (start, end+1) if is_prime(num)]
#
# # print(primes)
#
# is_prime(n)
#
# def find_index(arr, number):
#     if number in arr:
#         return arr.index(number)
#     else:
#         return -1
#
# arr, number = [1, 2, 3, 4, 5, 6, 7, 8, 9], 5
# index = find_index(arr, number)
# print(index)

# TODO 3: Hallo

1 zahlenliste = [2, 1, 5, 2, 10]
2 quadrate = [ zahl**2 for zahl in zahlenliste ]
3 print(quadrate)
