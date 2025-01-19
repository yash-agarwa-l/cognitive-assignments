import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

random_numbers = [random.randint(100, 900) for _ in range(100)]

odd_nums = []
even_nums = []
prime_nums = []

for num in random_numbers:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num) 
    
    if is_prime(num):
        prime_nums.append(num) 

# Print the results
print(f"Random Numbers: {random_numbers}")
print(f"Total Odd Numbers: {len(odd_nums)} are:  {odd_nums}")
print(f"Total Even Numbers: {len(even_nums)}  are:  {even_nums}")
print(f"Total Prime Numbers: {len(prime_nums)}  are:  {prime_nums}")
