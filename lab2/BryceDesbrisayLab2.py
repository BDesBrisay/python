'''
Bryce DesBrisay
CIS 117 - Lab 2
'''

# Get input from user
name = input("Enter Name: ")
gNumber = input("Enter ID: ")

# Prints basic text with input
print("My Family Name is " + name)
print("My Student ID is " + gNumber)

# Takes all of the numbers in the gNumber and adds them together
myId = sum(int(x) for x in gNumber if x.isdigit())

# Sets nLet equal to the length of your name
nLet = len(name)

# Prints out these values in a sentence
print("The value of myId is " + str(myId))
print("The number of characters in my last name is " + str(nLet))

# Assigns variables with values specified by the professor
expression1 = myId / 2
expression2 = myId % 2
expression3 = sum(list(range(2, nLet)))
expression4 = myId = nLet
expression5 = abs(nLet - myId)
expression6 = (myId) / (nLet + 1100)
expression7 = (nLet % nLet) and (myId * myId)
expression8 = 1 or (myId / 0)
expression9 = round(3.14, 1)

# Print out these values and round extra decimal points
print("Expression #1 -------------: " + str(expression1))
print("Expression #2 -------------: " + str(expression2))
print("Expression #3 -------------: " + str(expression3))
print("Expression #4 -------------: " + str(expression4))
print("Expression #5 -------------: " + str(expression5))
print("Expression #6 -------------: " + str(round(expression6, 2)))
print("Expression #7 -------------: " + str(expression7))
print("Expression #8 -------------: " + str(expression8))
print("Expression #9 -------------: " + str(expression9))

# The output
'''
Enter Name: Desbrisay
Enter ID: G01032992
My Family Name is Desbrisay
My Student ID is G01032992
The value of myId is 26
The number of characters in my last name is 9
Expression #1 -------------: 13.0
Expression #2 -------------: 0
Expression #3 -------------: 35
Expression #4 -------------: 9
Expression #5 -------------: 0
Expression #6 -------------: 0.01
Expression #7 -------------: 0
Expression #8 -------------: 1
Expression #9 -------------: 3.1
'''
