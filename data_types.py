# String data type

#literal assignment
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name # Concatination
# print(full_name)
# print(type(full_name))
# print(type(first_name) == str)
# print(isinstance(first_name, str))
full_name += " is a software engineer!" # Augmented assignment
# print(full_name)


# constructor assignment
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# Casting a number to a string
# decade = str(2026)
# print(type(decade))
# statement = "The year is " + decade + "'s period!"
# print(statement)

# Multiple lines
multiline = """This is a string that spans
multiple lines.

This is the end of the string.
                                Bye!"""
# print(multiline)

# Escaping special characters
# sentence = 'I\'m a software engineer!\tHey!\n\nWhere\'s this at\\located?'
# # print(sentence)

# # string methods
# print(first_name)
# print(first_name.upper())
# print(first_name.lower())

# print(multiline.title())
# print(multiline.replace("string", "ok"))
# print(multiline)


print(len(multiline))
multiline += "                                " # Adding whitespace to the end of the string
multiline = "                                 " + multiline #Adding whitespace to the beginning of the string
print(len(multiline))

print(len(multiline.strip())) # Removes whitespace from the beginning and end of the string
print(len(multiline.lstrip())) # Removes whitespace from the beginning of the string
print(len(multiline.rstrip())) # Removes whitespace from the end of the string

print(" ")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print(" ")

print ("Coffe".ljust(16,".") + "$5".rjust(4))
print ("Muffin".ljust(16,".") + "$10".rjust(4))
print ("croissant".ljust(16,".") + "$15".rjust(4))
print ("Burger".ljust(16,".") + "$5".rjust(4))


print(" ")

#string index values
print(first_name[1]) # prints the second character in the string
print(first_name[-1]) # prints the last character in the string
print(first_name[1:]) # prints the string from the second character to the second to last characterz


#some methods return boolean data
print(first_name.startswith("D")) # returns True if the string starts with the specified character
print(first_name.endswith("n")) # returns True if the string ends with the specified character


# Boolean data type
myvalue = True
X = bool(False)
print(type(X))
print(isinstance(myvalue, bool))


# Numeric data type

# integer data type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Floating point data type
rating = 4.9
y = float(3.14)
print(type(rating))
print(isinstance(rating, float))


# Complex type
complex_number = 2 + 3j
print(type(complex_number))
print(complex_number.real) # prints the real part of the complex number
print(complex_number.imag) # prints the imaginary part of the complex number




print(abs(complex_number * -2)) # returns the absolute value of a number


import math

print(math.pi) # prints the value of pi
print(math.sqrt(16)) # prints the square root of 16
print(math.ceil(3.14)) # prints the smallest integer greater than or equal to 3.14
print(math.floor(3.14)) # prints the largest integer less than or equal to 3.14


#castin a string to a number
zipcode = "711227"
zip_value = int(zipcode)
print(type(zip_value))