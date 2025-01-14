import math
import random

# RANDOM NUMBERS
#Write a program to generate 5 random numbers between 1 and 100 and print them.
i=1
while(i<=5):
    print(random.randrange(1, 101))
    i+=1
#9.2 Write a program to generate a random number and check if it is prime.
no=random.random()
if no <= 1:
    print("False")
for i in range(2, int(math.sqrt(no)) + 1):
    if no % i == 0:
        print("not PRime")
    if i==int(math.sqrt(no)):
        print("PRime")
#9.3 Write a program to simulate rolling a six-sided die.
while True:
    choice=int(input("1 for continuing, 0 for stopping "))
    if choice==0:
        break
    elif choice==1:
        print("Rolling die")
        print(random.randrange(1,7))
    else:
        print("Wrong choice")
        continue
#9.4 Write a program to shuffle a list of numbers.
arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr)
#9.5 Write a program to randomly select an item from a list.
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
#9.6 Write a program to generate a random password of given length.
length=int(input("Enter length of passwrd "))
passwd =random.randint(10**(length-1),10**length)
print(passwd)
#9.7 Write a program to pick a random card from a standard deck of 52 cards.
cards = ["Diamonds", "Spades", "Hearts", "Clubs"] 
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] 

card = random.choices(cards) 
rank = random.choices(ranks) 

print(f"The {rank} of {card}") 
