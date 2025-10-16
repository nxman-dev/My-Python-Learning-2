# Simple Python program to take name and date input from user and display a message

# Using string replacement to create a letter template
letter = "Dear <|NAME|>,\nYou are selected!\nDate of joining is <|DATE|>"

# Taking input from the user
name = input ("Enter your naem : ")

# Taking date input from the user
date = input ("enter date : ")

# Replacing placeholders with actual values
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

# Displaying the final letter
print (letter) 