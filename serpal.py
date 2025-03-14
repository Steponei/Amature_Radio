#=================================================================
#		RESISTORS IN SERIES OR PARALLEL
#		-------------------------------
#
# This program calculates the total resistance of
# serial or parallel connected resistors
#
# Program: sepal.py
# Date: March 25
#Author: 2E0HCY
#==================================================================
print("RESISTORS IN SERIES OR PARALLEL")
print("===============================")
yn = "y"

while yn == 'y':
    N = int(input("\nHow many resistors are there?: "))
    mode = input("Are the resistors series (s) or parallel (p)?: ")
    mode = mode.lower()
#
# Read the resistor values and calculate the total
#
    resistor = 0.0
    
    if mode == 's':
        for n in range(0,N):
            s = "Enter resistor" + str(n+1) + " value in Ohms: "
            r = int(input(s))
            resistor = resistor + r
        print("Total resistance = %d Ohms" %(resistor))
    elif mode == 'p':
        for n in range(0,N):
            s = "Enter resistor" + str(n+1) + "value in Ohms:"
            r = float(input(s))
            resistor = resistor +1 / r
        print("Total resistance = %.2f Ohm" %(1 / resistor))
#
# Check f user wants to exit
#
    yn = input("\nDo you want to continue?: ")
    yn = yn.lower()