#1: Famous Quote - DONE
#Find a quote from a famous person you admire. Write a function named famous_quote() that
#prints the quote and the name of its author."""

quote = '"Even I don´t wake up looking like Cindy Crawford"'
author = "Cindy Crawford"
print("Task 1: ", author, "once said", quote)

#2: Number Eight - DONE
# Write a function called number_eight(), that uses addition, subtraction, multiplication, division
# and exponentiation operations that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results.

def number_eight():
  print("Task 2:", 5 + 3, 10-2, 4*2, int(16/2), 2**3, sep=", ")

number_eight()

#3: Formatting
# Write a function name_age() that accepts the name and age of a person. It then prints it on the
# console in the following format:
# Hello, NAME. You are AGE years old

# def name_age():
#     name, age = input("Sag mir deinen Vornamen und dein Alter getrennt durch ein Leerzeichen.").split()
#     print("Hallo", str(name), "Du bist", int(age), "Jahre alt") #Concentation
#     print("Hallo", {}, "Du bist", {}, "Jahre alt".format(name, age)) #String format()
#     print(f"Hallo", {name}, "Du bist", {age}, "Jahre alt") #f-strings
#
# name_age()

#hier fehlermeldung falls nur ein name eingegeben wurde

#4: Swap - DONE
# Write a function swap_integers() that reads two integers from the user and prints them on the
# console. Then the function swaps the integers in memory and prints the swapped integers again on
# the console. If, for example, the first integer is x=10 and the second is y=20, x must have the value
# 20 after the swap (Hint: you can use a temporary variable). The function does not return anything.

# def swap_integers():
#     int1, int2 = input("Task 3: Sag mir bitte zwei Zahlen mit Leerzeichen getrennt: ").split()
#     print("    Vor Swap", int1,",", int2)
#     print("    Swap", int2, ",", int1)
#
# swap_integers()


#5: Modulo check - DONE
# Write a function check_numbers(number1, number2) that accepts two arguments. The
# function checks if any of the numbers is divisible by 6 and if both are divisible by 10. The function
# does return true if both conditions are true. Hint: Use the modulo operator.

num1, num2 = (30, 10)
def check_number(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        print("Task 5:", True)
    elif num1 % 6 == 0 or num2 % 6 == 0:
        print("Task 5: At least on number is divisible by 6")
    elif num1 % 10 == 0 and num2 % 10 == 0:
        print("Task 5: Both numbers are divisible by 10")
    else:
        print("Task 5: Not divisible by 6 or by 10")

check_number(num1, num2)

#6: Summarizer
# Write a function sum_up(number1, number2) that accepts two integers and sums up every
# integer between the two numbers including the given integers (inclusive). Check if the second
# number is greater than the first and display a message if it’s not. The function returns the result as an
# integer
#
# num1, num2 = (3, 9)
# def sum_up(num1, num2):
#
#
# sum_up(num1, num2)


#7: Sequencer
# Write a function sequence(number) that accepts an integer as argument. It then checks if the
# given number is an integer between 0 and 9 (inclusive) and prints an error message if it’s not. In case
# the given number is between 0 and 9, the function prints the sequence of number from 0 to 9 on the
# console without the given number. The function does not return anything.

number = input("Sag mir eine Zahl. Wenn Du willst, das was Cooles passiert sag mir eine Zahl zwischen 0 und 9: ")
def sequence(number):
    if int(number) < 0 or int(number) > 9:
        number = input("Nochmal: wenn Du willst, das was Cooles passiert, sag mir eine Zahl zwischen 0 und 9: ")
    else:
        for i in range(10):
            if i != number:
                print(i, end=" ")

sequence(number)

#hier soll die schleife unendlich sein

#8: String Check
# Write a function check_string(text) that accepts a string and checks if it begins OR ends with
# the character “a”. Use built-in string methods of python. The function returns True if the string begins or ends with an “a”. The function should work for
# lower and upper case strings.

text = "nichts oder alles"

def check_string(text):
    if text.endswith("a" or "A") or text.startswith("a" or "A"):
        print("Task 8: ", True)
    else: print ("Task 8:", False)

check_string(text)

#9: ASCII Art - DONE
# Write a function triangle(rows) that accepts an integer and prints out a triangle of stars with
# spaces in between them with the height of the given integer. The function does not return anything.not
rows = int(6)
print("Task 9: ")
def triangle(rows):
   for stars in range(1, rows+1):
        print(" "*(rows-1) + "* "*stars)

triangle(rows)





