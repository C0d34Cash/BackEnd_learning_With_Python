# Assignment operator
X = 5 
X += 2
Y = 10
Y -= 3
print(Y)
print(X)

# Arithmatic Operators
X = input("Enter your first number: ")
X = int(X)
Y =input ("Enter your second number: ")
Y = int(Y)

Z = X + Y # Addition
print("The sum of your two numbers is: " + str(Z))

W = Y / X # Division
print("The division of your two numbers is: " + str(round(W)))

T = X * Y # Multiplication
print("The multiplication of your two numbers is: " + str(T))

U = X - Y # Subtraction
print("The subtraction of your two numbers is: " + str(U))

V = Y % X # Remainder
print("The remainder of your two numbers is: " + str(V))

B = X ** Y # Exponent
print("The exponent of your two numbers is: " + str(B))

X == Y # Comparison Operators
print("Are the two numbers equal: " + str(X == Y))

X != Y # Comparison Operators
print("Are the two numbers not equal: " + str(X != Y))

X > Y # Comparison Operators
print("Is the first number greater than the second number: " + str(X > Y))

X < Y # Comparison Operators
print("Is the first number less than the second number: " + str(X < Y))


#Boolean Operators
X = True
Y = False
Z = True
W = False
print(not X) # NOT operator
print(W and Z) # AND operator
print(X or Y) # OR operator
print(not(X and Y)) # NOT AND operator
print(not(W or Z)) # NOT OR operator
print((X and Y) or (Z and W)) # AND OR operator
print((X or Y) and (Z or W)) # OR AND operator
print((X and Y) or (Z and W) and (X or Y)) # AND OR AND operator
print((X and not Y) or (not X and Y)) # X-OR Operator

# Way 1: using not and XOR
print(not ((X and not Y) or (not X and Y)))

# Way 2: using == (easiest)
print(X == Y)

# Way 3: using not != 
print(not (X != Y))

#Ternary Operator
print("Right on") if X>10 else print("Wrong on")


