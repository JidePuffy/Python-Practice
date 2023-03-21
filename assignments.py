# x = "Hello World!"
# print(x)

#Assignment 2
#Write a program that asks a user for their favorite color, then allow them to type in their color... 
# Finally, have the program respond to them by displaying the text "Your favorite color is" followed by the color they typed.

# fav_color = input("Enter favorite color here")
# print ("Your favorite color is " + fav_color)

#Assignment 3
#Prompt the user for their first name. Then, prompt them for their last name. 
# Display the text back all on one line saying, "Your name is last-name, first-name, last-name"

# first_name = input("Please enter your first name ")
# last_name = input("Please enter your last name ")
# output = f"Your name is  {last_name}, {first_name} {last_name}"
# print(output)

# Assignment 4
# Write a program to prompt the user for the following:

# First name

# Last name

# Email Address

# Phone Number

# Job Title

# ID Number

# Then you should display the information back in this format:

# Note that the square brackets [] indicate a value coming from the user and should not be displayed.


# ----------------------------------------
# [LAST NAME], [first name]
# [Job title]
# ID: [id number]

# [email address]
# [phone number]
# ----------------------------------------
# In addition to the spacing and punctuation shown above, you must implement the following requirements:

# The last name should be converted from whatever the user types to be displayed in ALL CAPS.

# The job title should be displayed so that the first letter is capitalized.

# The email address should be displayed in all lowercase.

# An example of the program running is shown:


# Please enter the following information:

# First name: Jane
# Last name: Doe
# Email address: JaneDoe@email.com
# Phone number: (208) 555-1234
# Job title: chief software architect
# ID Number: 83-23821

# The ID Card is:
# ----------------------------------------
# DOE, Jane
# Chief Software Architect
# ID: 83-23821

# janedoe@email.com
# (208) 555-1234
# ----------------------------------------
# CORE REQUIREMENTS
# Each team activity will contain three core requirements... 
#These are items that you are expected to be able to complete during the one hour team meeting if you have come prepared.

# You should work through the assignment in this order:

# Prompt for all of the necessary values and store them in variables...
#Then display each item to the screen, without worrying about any spacing, punctuation, or formatting yet.

# Arrange the display so that the spacing and punctuation exactly match the example shown.

# Use the built-in string functions to make the last name display in all caps, the job title display in "title case," and 
#the email display in all lowercase.

# STRETCH CHALLENGE
# Most team activities will also contain stretch challenges, which are not specifically required by the assignment, 
#but are a great way to dive deeper into the material. 
#They can be more difficult and may require you to find solutions that weren't directly covered in the preparation material.

# The stretch challenges for this activity are:

# Add hair color and eye color and put them both on the same line in the display.

# Add a field for the name of the month they started and also a yes/no field for whether they have completed advanced training. 
#Put these both on the same line in the display.

# For the two lines that you just added, make it so that the second columns align, regardless of how many letters are in the responses.

# To complete this one, you may need to search the internet for something like, "python spacing format" or 
#something similar to see if you get any ideas.

# At the end of the stretch challenge, your output should look something like the following:


# The ID Card is:
# ----------------------------------------
# DOE, Jane
# Chief Software Architect
# ID: 83-23821

# janedoe@email.com
# (208) 555-1234

# Hair: Brown           Eyes: Blue
# Month: September      Training: Yes

first_name = input("Please enter your first name here")
last_name = input("Please enter your last name here")
email = input("Please enter your email here")
phone_number = input("Pleae enter your phone number here")
job_title = input("Please enter your job title here")
id_number = input("Please enter your identity number here")


hair_color = input("Please enter your hair colour:")
eye_color = input("Please enter your eye color:")
month = input("Please enter your month of birth:")
training = input("Do you have any training on this field? True/False")
if training == True:
    print("Yes")
else:
    print("No")

output =f"{last_name.upper()}, {first_name.lower()} \n{job_title.capitalize()} \nID:{id_number} \n\n{email.lower()} \n{phone_number} \nHair:{hair_color}'       'Eyes:{eye_color} \nMonth:{month} '     'Training:{training}" 
print(output)




