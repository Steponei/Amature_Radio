#==================================================================
#	RESISTOR COLOURS CODES
#   ----------------------
#
# The user enters the three colours of a resistor
# and the program calculates and dispays the value
# of the resistor in Ohms. The program identifies all
# types of resistors with 4 colour bands
#
# Program: resistor2.py
# Date	 : March 2025
# Author : 2E0HCY
#==================================================================
colours = ['black','brown','red','orange','yellow','green', \
'blue','violet','grey','white', 'gold', 'silver']

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
    if ThirdValue == 10:
        Resistor = Resistor / 10.0
        print ("Resistance = %3.2f Ohms" % (Resistor))
    elif ThirdValue == 11:
        Resistor = Resistor/100.0
        print ("Resistor = %3.2fOhms" % (Resistor))
    else:
        Resistor = Resistor * (10 ** ThirdValue)
        print("Resistance = %d Ohms" % (Resistor))
#
#	Ask for more
#

    yn = input("\nDo you want to continue?: ")
    yn =  yn.lower()


