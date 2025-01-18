# 5.1 Find the largest and smallest numbers in a list
numbers = [10, 25, 8, 42, 19]
print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")

# 5.2 Retrieve the value of a given key from a dictionary
data = {"name": "Alice", "age": 25, "city": "New York"}
key = input("Enter the key to retrieve its value: ")
value = data.get(key, "Key not found")
print(f"Value: {value}")

# 5.3 Sort a list of numbers in ascending and descending order
numbers = [32, 10, 45, 78, 5]
numbers_asc = sorted(numbers)
numbers_desc = sorted(numbers, reverse=True)
print(f"Ascending order: {numbers_asc}")
print(f"Descending order: {numbers_desc}")

# 5.4 Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"Merged dictionary: {merged_dict}")
