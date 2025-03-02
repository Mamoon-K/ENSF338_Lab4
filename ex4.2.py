import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Inefficient Search: Linear Search (O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient Search: Iterative Binary Search (O(log n))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

"""
Linear Search: In the worst case, the target is at the end or not present, so O(n) complexity.
Binary Search: In the worst case, the search space halves each iteration, so to O(log n) complexity.
"""

# The following code is from GPT4o
# Generate a large sorted array (10000 elements)
arr = list(range(10000))

# Number of trials (100 measurements)
num_trials = 100

# Store execution times
linear_times = []
binary_times = []

# Conduct the experiment
for _ in range(num_trials):
    target = random.choice(arr)  # Pick a random target

    # Measure Linear Search time
    start = time.time()
    linear_search(arr, target)
    linear_times.append(time.time() - start)

    # Measure Binary Search time
    start = time.time()
    binary_search(arr, target)
    binary_times.append(time.time() - start)

# Plot the results
plt.figure(figsize=(10, 5))
plt.hist(linear_times, bins=20, alpha=0.7, label="Linear Search", edgecolor='black')
plt.hist(binary_times, bins=20, alpha=0.7, label="Binary Search", edgecolor='black')
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Frequency")
plt.title("Execution Time Distribution: Linear vs Binary Search")
plt.legend()
plt.show()