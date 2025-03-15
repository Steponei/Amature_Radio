#=============================================================================
#							TUNE TO FM FREQUENCY
#							====================
#
# This program tunes to an FM frequency (WBFM) using the RTL_FM
#
# Author: 2E0HCY
# File	: simpleFM.py
# Date	: March 2025
#=============================================================================
import os
print("")
print("SimpleFM - Tune to a FM frequency")
print("=================================")
print("")

freq = 1000.0*float(input("Enter the FM frequency (kHz): "))
frequency = str(freq)
rtl = "rtl_fm -m wbfm -f" + frequency + " | aplay _r 32000 -fs16_LE -c 1"
os.system(rtl)