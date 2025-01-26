import pandas as pd
df= pd.read_csv('/Users/yashagarwal/Downloads/employees.csv')
# print(df)

row, col = df.shape
# print(row,col)

# print(df.describe())

# df.head(5)
# df.tail(3)

print(df["Salary"].mean())
print(df["Bonus"].sum())
print(df.Age.min())
print(df["Rating"].max())
print(df.sort_values(by="Salary",ascending=True))

#  e) Calculate the following statistics from the dataset:
# i. The average salary of employees.
# ii. The total bonus paid to all employees.
# iii. The youngest employee's age.
# iv. The highest performance rating.
# f) Sort the DataFrame by the Salary column in descending order.

# g) Add a new column that categorizes employees based on their performance rating:
# i. Excellent for ratings >= 4.5
# ii. Good for ratings >= 4.0 but < 4.5
# iii. Average for ratings < 4.0
# h) Identify missing values in the DataFrame.
# i) Rename the Employee_ID column to ID.
# j) Find all employees who:

# i. Have more than 5 years of experience.
# ii. Belong to the IT department.

# k) Modify the dataset by adding a new column, Tax, which deducts 10% of the
# Salary.
# l) Save the modified DataFrame (with added columns) to a new CSV file.