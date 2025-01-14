# EXCEPTION HANDLING
#8.1
i=0
try: 
  x=9/i
  print(x)
except:
  print("Tried to diivide by zero")
#8.2
num = input("Please enter a number: ")
try:    
    number = int(num)
    print(f"You entered the number: {number}")
except ValueError:
    print(f"Invalid input '{num}' ")
#8.3
try: 
  x=9/i
  print(x)
except:
  print("Something went wrong")
finally:
  print("Moving on")
