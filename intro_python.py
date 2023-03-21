#PRINT
#print("Hello World")
#print("You can use double quote")
#print('You can use single quotes')
#The input function is used in asking information from the user:
#name = input("Enter your name:")
#print(name)

#BLANK LINES
#Blank lines are needed so that what we type wont be clustered.
#print("Can you see the blank line \nin the middle?")

#COMMENTS
#Comments in python starts with a hashtag and does not reflect when the program is run. It only helps in documenting steps and debugging as well.
#Shortcuts for commenting and uncommenting = Ctrl + k and ctrl + ku respectively.

#STRINGS
#variables are placeholders for their values
#More than one variable can be joined together using the '+' sign.
#first_name = "jide "
#last_name = "Okeke"
#print(first_name + last_name)
#print("Hello  " +first_name +" "+ last_name)

#CAPITAL AND SMALL LETTERS
#To change the casing or count the number of alphabets in a sentence, we use .upper, .lower, .capitalize, .count
#sentence = "Hello World"
#print(sentence . upper())
#print(sentence . lower())
#print(sentence . capitalize())
#print(sentence . count("l"))

#son1_name = input("Name of first son:")
#Son2_name = input("Name of second son:")

# first_name = input("What is your first name?")
# last_name = input("What is your last name?")


# print("Hello! " + first_name + " "+ last_name)
# print("Hello! " + first_name .upper() + " "+ last_name.capitalize())

#LISTS AND SLICES AND INDEXING
#List is a data type used in grouping values together. Usually separated by commas in-between square brackets'[]'
#Lists, like strings can be indexed and sliced.

# squares = [1, 4, 9, 16, 25]
# print(squares)
# print(squares[0]) #indexing returns the item
# print(squares[-1])
# print(squares[-3:])#slicing returns a slice of the list

# numb_above_20 = [21, 22, 23, 24, 25, 26, 27, 28, 29]
# print(squares + numb_above_20)

# together = [1, 4, 9, 16, 25], [21, 22, 23, 24, 25, 26, 27, 28, 29]
# print(together[1][5])

# pi = 3.14159
# days_in_march = "31 "
# print(days_in_march + "Total days in march.")
# days_in_march = 31
# print(days_in_march + "Total days in march.") #cannot concantenate a string with an integer

#DATE AND TIME FOR LOGGING
#To get date and time
#We need to use the datetime library
#From datetime import datetime
from datetime import datetime, timedelta
#now = datetime.datetime.now()
#print(now)
#the now function returns a datetime object
#print("Today is: " + str(now))
#timedelta represents a duration of time. It allows you to specify a period of time.
#You can use timedelta to add or remove days
today = datetime.now()
one_day = timedelta(days=1)
yestarday = today - one_day
print(yestarday)

yestarday = now - one