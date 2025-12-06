import numpy as np


numbers = [10, 25, 7, 42, 18]

arr = np.array(numbers)


mean_value = np.mean(arr)
max_value = np.max(arr)
sum_value = np.sum(arr)


print("list:", numbers)
print("NumPy array:", arr)
print("Mean:", mean_value)
print("Max value:", max_value)
print("Sum:", sum_value)
