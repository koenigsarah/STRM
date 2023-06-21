# 1: Famous Quote - DONE
"""Find a quote from a famous person you admire. Write a function named famous_quote() that
prints the quote and the name of its author."""


def famous_quote():
    quote = '"Even I don´t wake up looking like Cindy Crawford"'
    author = "Cindy Crawford"
    print("Task 1: ", author, "once said:", quote, "\n")

famous_quote()

print("Hallo Ö3!")

# 2: Number Eight - DONE
"""Write a function called number_eight(), that uses addition, subtraction, multiplication, division
and exponentiation operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results."""


def number_eight():
    print("Task 2.1: ", 5 + 3, 10 - 2, 4 * 2, int(16 / 2), 2 ** 3, sep=" ")


number_eight()


# ODER:

def number_eight():
    a = 5 + 3
    b = 10 - 2
    c = 4 * 2
    d = 2 ** 3
    e = int(16 / 2)
    print("Task 2.2: ", a, b, c, d, e, sep=" ")


number_eight()
print()


# 3: Formatting - DONE
# Write a function name_age() that accepts the name and age of a person. It then prints it on the
# console in the following format:
# Hello, NAME. You are AGE years old

def name_age():
    name, age = input("Task 3: Sag mir deinen Vornamen und dein Alter getrennt durch ein Leerzeichen: ").split()
    age_as_int = int(age)
    message = "Hallo " + name + " Du bist " + age + " Jahre alt"  # Concentation(Nachteil: nur Strings)
    print(message)
    print("Hallo {name} Du bist {age} Jahre alt".format(name=name, age=age_as_int))  # String format()
    print(f"Hallo {name} Du bist {age_as_int} Jahre alt", "\n")  # f-strings


name_age()

# Verbesserungsvorschlag: hier fehlermeldung falls nur ein name eingegeben wurde

# 4: Swap - DONE
""" Write a function swap_integers() that reads two integers from the user and prints them on the
console. Then the function swaps the integers in memory and prints the swapped integers again on
the console. If, for example, the first integer is x=10 and the second is y=20, x must have the value
20 after the swap (Hint: you can use a temporary variable). The function does not return anything."""


def swap_integers():
    int1, int2 = input("Task 4: Sag mir bitte zwei Zahlen mit Leerzeichen getrennt: ").split()
    print("    Vor Swap ", int1, ",", int2)
    z = int1
    int1 = int2
    int2 = z
    print("    Nach Swap", int1, ",", int2, "\n")


swap_integers()

# 5: Modulo check - DONE
"""Write a function check_numbers(number1, number2) that accepts two arguments. The
function checks if any of the numbers is divisible by 6 and if both are divisible by 10. The function
does return true if both conditions are true. Hint: Use the modulo operator."""

num1, num2 = (12, 10)
print("Task 5: ")


def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        return True
    else:
        return False


print(check_numbers(num1, num2), "\n")

# oder nur: return if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0)

# Andere Variante:
# #    print("Task 5: ")
#     if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
#         return True
#     elif num1 % 6 == 0 or num2 % 6 == 0:
#         print("Task 5: At least on number is divisible by 6")
#     elif num1 % 10 == 0 and num2 % 10 == 0:
#         print("Task 5: Both numbers are divisible by 10")
#     else:
#         print("Task 5: Not divisible by 6 or by 10")

# 6: Summarizer DONE
"""Write a function sum_up(number1, number2) that accepts two integers and sums up every
integer between the two numbers including the given integers (inclusive). Check if the second
number is greater than the first and display a message if it’s not. The function returns the result as an
integer"""

num1, num2 = (3, 9)
print("Task 6: ")


def sum_up(num1, num2):
    if num1 > num2:
        print("Nummer 2 sollte größer als Nummer 1 sein")
    else:
        summe = 0
        for i in range(int(num1), int(num2 + 1)):
            summe += i
        return summe


print(sum_up(num1, num2), "\n")

# Notizen
#         return summe
#             print("Task 6:", summe, type(summe))
#
# sum_up(num1, num2)

# 7: Sequencer DONE
"""Write a function sequence(number) that accepts an integer as argument. It then checks if the
given number is an integer between 0 and 9 (inclusive) and prints an error message if it’s not. In case
the given number is between 0 and 9, the function prints the sequence of number from 0 to 9 on the
console without the given number. The function does not return anything."""

number_ = input(
    "Task 7: Sag mir eine Zahl. Wenn Du willst, das was Cooles passiert, sag mir eine Zahl zwischen 0 und 9: ")


def sequence(number):
    if int(number) < 0 or int(number) > 9:
        print("Das ist keine Zahl zwischen 0 und 9. Pech gehabt!")
    else:
        for i in range(0, 10):
            if i != number:
                print(i, end=" ")  # end ein Leerzeichen ans Ende des Arguments
        print()


sequence(int(number_))

print()

# Verbesserungsvorschlag für mich später: hier soll die Schleife unendlich sein, also wenn Zahl < 0 oder > 9 eingegeben wird, soll weiter gefragt werden
# def sequence(number):
#     if int(number) < 0 or int(number) > 9:
#         print("Das ist keine Zahl zwischen 0 und 9. Pech gehabt!")
#     else:
#         for i in range(10):
#             if i == int(number):continue
#             print(i)
# sequence(number)

# 8: String Check DONE - FALSCH, nochmal
"""Write a function check_string(text) that accepts a string and checks if it begins OR ends with
the character “a”. Use built-in string methods of python. The function returns True if the string begins or ends with an “a”. The function should work for
lower and upper case strings."""

text = "lle"


def check_string(text):
    return text.endswith("A") or text.endswith("a") or text.startswith("A") or text.startswith("a")

check_string(text)

print("Task 8: ", check_string(text), "\n")

# Vorher:
# text = "alles"
# def check_string(text):
#     if text.endswith("a" or "A") or text.startswith("a" or "A"):
#         print("Task 8: ", True)
#     else:
#         print("Task 8:", False)

check_string(text)

# 9: ASCII Art - DONE
"""Write a function triangle(rows) that accepts an integer and prints out a triangle of stars with
spaces in between them with the height of the given integer. The function does not return anything.not"""

rows = int(6)
print("Task 9: ")


def triangle(rows):
    for stars in range(1, rows + 1):
        print(" " * (rows - 1) + "* " * stars)


triangle(rows)
