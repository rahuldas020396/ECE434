#!/bin/sh

config-pin P9_19 i2c
config-pin P9_20 i2c

temp=`i2cget -y 2 0x48`
#comment
#echo = print
# $ to get the value of a variable
# read stores user input
# man for manual page

temp1=`i2cget -y 2 0x48`
temp2=`i2cget -y 2 0x4a`

#Displaying current Temperature
echo -n "Temp Sensor 0x48: "
echo -n $(($temp1*18/10+32))
echo -n 'F or '
echo -n $((temp1))
echo -n 'C'
echo ''

echo -n 'Temp Sensor 0x4a: '
echo -n $(($temp2*18/10+32))
echo -n 'F or '
echo -n $((temp2))
echo 'C'
echo ''

#writing to the thigh and tlow
#tlow
i2cset -y -r 2 0x48 0x02 21
i2cset -y -r 2 0x4a 0x02 21
#thigh
i2cset -y -r 2 0x48 0x03 23
i2cset -y -r 2 0x4a 0x03 23

#i2cset -y -r 2 0x48 0x01 0x80
i2cset -y -r 2 0x48 0x01 0x00