#==================================================================
#	RESISTOR COLOURS CODES
#    ----------------------
#
# The user enters the three colours of a resistor
# and the program calculates and dispays the value
# of the resistor in Ohms
#
# Program: resistor.py
# Date	 : March 2025
# Author : 2E0HCY
#==================================================================
colours = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']


print("RESISTOR VALUE CALCULATOR")
print("=========================")
yn = "y"

while yn =='y':
    FirstColour = input("Enter First Colour: ")
    SecondColour = input("Enter Second Colour: ")
    ThirdColour = input("Enter Third Colour: ")
#
#	Convert to lower case
#
    FirstColour = FirstColour.lower()
    SecondColour = SecondColour.lower()
    ThirdColour = ThirdColour.lower()
#
#	Find the values of colours
#
    FirstValue = colours.index(FirstColour)
    SecondValue = colours.index(SecondColour)
    ThirdValue = colours.index(ThirdColour)
#
#	Now calculate the value of the resistor
#
    Resistor = 10 * FirstValue + SecondValue
    Resistor = Resistor * (10 ** ThirdValue)
    print ("Resistor = %d Ohms" % (Resistor))
#
#	Ask for more
#

    yn = input("\nDo you want to continue?: ")
    yn =  yn.lower()

