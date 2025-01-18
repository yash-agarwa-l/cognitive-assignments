import os
import sys
import math
import random
import datetime

# USE OF LIBRARIES
#11.1
findSqrt=int(input("enter number to find sqrt of:"))
print("Sqrt is : ",math.sqrt(findSqrt))
#11.2
currTime = datetime.datetime.now()
print(currTime)
#11.3
current_working_directory = os.getcwd()
content = os.listdir(current_working_directory) 
print("current working directory has :",content)
    
