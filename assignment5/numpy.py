import numpy as np
import matplotlib.pyplot as plt

# Q.1 Operations on Matrix gfg
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
sum_elements = np.sum(gfg)
row_sum = np.sum(gfg, axis=1)
col_sum = np.sum(gfg, axis=0)

print("Q1 - Sum of all elements:", sum_elements)
print("Q1 - Sum of all elements row-wise:", row_sum)
print("Q1 - Sum of all elements column-wise:", col_sum)

# Q.2 Operations on NumPy Array
array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)
sorted_indices = np.argsort(array)
smallest_4 = np.partition(array, 4)[:4]
largest_5 = np.partition(array, -5)[-5:]

print("\nQ2 - Sorted array:", sorted_array)
print("Q2 - Indices of sorted array:", sorted_indices)
print("Q2 - 4 smallest elements:", smallest_4)
print("Q2 - 5 largest elements:", largest_5)

# Integer and Float Elements
array2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integers = array2[array2 == array2.astype(int)]
floats = array2[array2 != array2.astype(int)]

print("\nQ2b - Integer elements:", integers)
print("Q2b - Float elements:", floats)

# Q.3 Personalized Sales Dataset
initials_ascii_sum = 65 + 66  # 'A' + 'B'
X = initials_ascii_sum  # X = 131
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
tax_rate = ((X % 5) + 5) / 100
sales_with_tax = sales * (1 + tax_rate)

discounted_sales = np.where(sales < X + 100, sales * 0.95, sales * 0.90)

sales_matrix = np.tile(sales, (3, 1))  # Stack sales data for three weeks
sales_matrix_with_increase = sales_matrix * (1 + 0.02) ** np.arange(3)[:, None]  # 2% increase per week

print("\nQ3 - Sales with tax applied:", sales_with_tax)
print("Q3 - Discounted sales:", discounted_sales)
print("Q3 - Sales for three weeks with increase:", sales_matrix_with_increase)

# Q.4 Plotting Functions
x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 1)

plt.figure(figsize=(10, 6))

# Plot y = x^2
plt.subplot(2, 2, 1)
plt.plot(x, y1, label="y = x^2")
plt.title("y = x^2")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")

# Plot y = sin(x)
plt.subplot(2, 2, 2)
plt.plot(x, y2, label="y = sin(x)")
plt.title("y = sin(x)")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")

# Plot y = exp(x)
plt.subplot(2, 2, 3)
plt.plot(x, y3, label="y = e^x")
plt.title("y = e^x")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")

# Plot y = log(|x| + 1)
plt.subplot(2, 2, 4)
plt.plot(x, y4, label="y = log(|x| + 1)")
plt.title("y = log(|x| + 1)")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")

plt.tight_layout()
plt.show()
