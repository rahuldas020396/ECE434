#!/bin/bash
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'ImageMagick\nhw04\n' \
     -draw "text 0,100 'Rahul'" \
     -draw "text 0,150 'has completed the'" \
     -draw "text 0,200 'ECE434 grind'" \
     $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE