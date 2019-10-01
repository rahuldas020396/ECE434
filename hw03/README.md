Files included:
1. Alert.py
	This program interfaces with the TI TMP101 sensors and sets an alert bit 
	high when the temperature either exceeds Thigh or falls below Tlow.
	(This program is unabe to toggle the bit however it is able to set the bit
	 active high or active low)
2. readTemp.sh
	This shell file prints the current temperature read by both the temp101
	sensors and also sets up the Thigh and Tlow registers
3. etchMatrix.py
	This program interfaces with the rotary encoders and the 8x8 bicolor
	LED marix. The etch a sketch can be played with the rotary encoders.

## Prof. Yoder's comments

Looks good.  Too bad you didn't get the alert pin figured out.

Grade:  10/10