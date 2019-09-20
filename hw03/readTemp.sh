#!/bin/sh

temp=`i2cget -y 2 0x48`
#comment
#echo = print
# $ to get the value of a variable
# read stores user input

temp1=`i2cget -y 2 0x48`
temp2=`i2cget -y 2 0x4a`

echo -n "Temp Sensor 0x48: "
echo $(($temp1*18/10+32))

echo -n 'Temp Sensor 0x4a: '
echo $(($temp2*18/10+32))