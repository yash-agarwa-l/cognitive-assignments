# 2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and  perform the following operations using tuple functions:  
# i. Identify the highest score and its index in the tuple.  
# ii. Find the lowest score and count how many times it appears.  
# iii. Reverse the tuple and return it as a list.  
# iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and  print its first occurrence index, or a message saying it’s not present.  

scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)


# i. Identify the highest score and its index in the tuple.
maxIndex = 0
for i in range(0,len(scores),1):
    if scores[i] > scores[maxIndex]:
        maxIndex= i
        
print(f"Max element is  {scores[maxIndex]} at index {maxIndex}" )
# or
maxVal = max(scores)
index= scores.index(maxVal)
print(f"Max element is  {maxVal} at index {index}" )




# ii. Find the lowest score and count how many times it appears.  
min_index = 0
for i in range(0,len(scores),1):
    if scores[i] < scores[min_index]:
        min_index= i
        
        
count = 0
for i in scores:
    if i == scores[min_index]:
        count = count + 1
        
print(f"no of times {scores[min_index]} is {count}")
#OR
print(f"no of times {min(scores)} is {scores.count(min(scores))}")



# iii. Reverse the tuple and return it as a list.  
scores_list= list(scores[::-1])
print(scores_list)
        
        
# iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and  print its first occurrence index, or a message saying it’s not present.
num= int(input("Enter a number: "))
if num in scores:
    print(f"First occurrence of {num} is at index {scores.index(num)}")
else:
    print("Number not found")
