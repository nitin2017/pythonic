#This is script to understand the escape sequence
##### ESCAPE SEQUENCE ####|||||#####   MEANING
##         \'         ####|||||#####   single quote
##         \"         ####|||||#####   double quote
##         \\         ####|||||#####   backslash
##         \n         ####|||||#####   new line
##         \t         ####|||||#####   tab
##         \b         ####|||||#####   backspace

print (' Hi I\'m Nitin') # Escape sequence to include single quote within single quote
print (" Hi I am \"Nitin\"") # Escape sequence to include double quotes within double quotes
print (" Hi I am Nitin \n I am using new line escape sequence here") # Escape sequence to use new line character
print (" Hi I am Nitin \t I am using table escape sequence") # Escape sequence to include tab character
# print (" This is backslash\")     #This will not work and will throw EOL Error
print (" This is backslash \\")
print (" This is double backslash \\\\")
print (" Helll\bo") # This is backspace escape sequence
