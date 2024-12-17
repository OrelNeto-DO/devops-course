#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Usage: $0 num1 operator num2"
  exit 1
fi

num1=$1
operator=$2
num2=$3

case "$operator" in
+) echo "Result: = $(( num1 + num2 ))"
;;
-) echo "Result: = $(( num1 - num2 ))"
;;
\*) echo "Result: = $(( num1 * num2 ))"
;;
/) if [ "$num2" -ne 0 ]; then
 echo "Result: = $(( num1 / num2 ))"
 else
      echo "Error: Division by zero is not allowed."
    fi
;;
esac
