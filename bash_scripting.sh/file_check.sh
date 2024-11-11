#!/bin/bash

read -p "Lets check if we have the file you are looking for... " file

#if [ -z "$1" ]; then
#	echo "Please provide a filename"
#	exit 1
#fi

#file="$1"

if [ -e "$file" ]; then
echo "file exist"
else 
echo "file doesn't exist"
fi

