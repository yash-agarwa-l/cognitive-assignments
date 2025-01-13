# 3.1 Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num< 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 3.2 Check if a given number is odd or even
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
