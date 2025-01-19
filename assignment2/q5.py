# 5. Write a program to rename a key city to a loca􏰀on in the following dic􏰀onary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)
