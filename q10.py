# COMMAND LINE ARGUMENTS

import sys

#10.1 Write a program to accept two numbers as command-line arguments, add them, and print the result.
x=int(sys.argv[1])
y=int(sys.argv[2])
sum=x+y
print("The addition is :",sum)
#10.2 Write a program to accept a string as a command-line argument and print its length.
cmdStr=sys.argv[1]
print(f"its length is {len(cmdStr)}")


