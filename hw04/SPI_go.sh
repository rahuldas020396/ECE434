#!/bin/bash
sudo ./on_180.sh
sleep 5
sudo fbi -noverbose -T 1 -a tux.png
sleep 10
sudo ./off.sh
sleep 5

# turning it 90 degrees
sudo ./on_90.sh
sleep 5
sudo fbi -noverbose -T 1 -a tux.png
sleep 10
sudo ./text.sh
sleep 10
sudo mplayer RedsNightmare.mpg
./off.sh
