#!/bin/bash 
COUNTER=0
while [  $COUNTER -lt 10000 ]; do
	echo The counter is $COUNTER
	make
	let COUNTER=COUNTER+1 
done
