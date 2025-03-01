
#1) The growth strategy for python lists is an over-allocation strategy, where a new list is created when the current list is full.
# This strategy allows for efficient memory usage, as it avoids reallocating memory frequently.
#The new size is computed as:
#new_allocated = newsize + (newsize/8) + 6 
#newsize >> 3 → Increases size by ~12.5% (same as newsize / 8).
#+6 → Adds extra padding to reduce reallocations.
#&~(size_t)3 → Ensures the size is a multiple of 4 for memory alignment.
#This ensures that each list expansion is not too aggressive, avoiding excessive memory usage, but still provides amortized O(1) append performance.
#Between lines 60 and 86 (including comments)

import sys
import time
import matplotlib.pyplot as plt

# Step 2: Track list capacity changes
def track_list_growth():
    lst = []
    prev_capacity = sys.getsizeof(lst)
    print(f"Initial list size: {prev_capacity} bytes")
    
    for i in range(64):
        lst.append(i)
        new_capacity = sys.getsizeof(lst)
        if new_capacity != prev_capacity:  # Capacity changed
            print(f"Capacity increased at {i} elements: {new_capacity} bytes")
            prev_capacity = new_capacity
    return lst

# Step 3 & 4: Measure time taken to grow from S to S+1 and S-1 to S
def measure_growth_time(lst, num_trials=1000):
    
    # Measure time from S to S+1
    time_s_to_s1 = []
    for _ in range(num_trials):
        temp_lst = lst.copy()
        start = time.perf_counter()
        temp_lst.append(0)
        end = time.perf_counter()
        time_s_to_s1.append(end - start)

    # Measure time from S-1 to S
    time_s1_to_s = []
    for _ in range(num_trials):
        temp_lst = lst[:-1]
        start = time.perf_counter()
        temp_lst.append(0)
        end = time.perf_counter()
        time_s1_to_s.append(end - start)

    return time_s_to_s1, time_s1_to_s

# Step 5: Plot results
def plot_results(time_s_to_s1, time_s1_to_s):
    plt.hist(time_s_to_s1, alpha=0.5, label="S to S+1")
    plt.hist(time_s1_to_s, alpha=0.5, label="S-1 to S")
    plt.legend()
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Time Distribution of List Expansion")
    plt.show()

# Run tests
lst = track_list_growth()
time_s_to_s1, time_s1_to_s = measure_growth_time(lst)
plot_results(time_s_to_s1, time_s1_to_s)


#5) The list growth time distribution shows that the time taken to expand from S to S+1 
# is slightly longer than the time taken to expand from S-1 to S. 
# This happens because when a list exceeds its allocated capacity, 
# Python reallocates a larger block of memory and copies existing elements, 
# making growth more expensive. In contrast, shrinking the list 
# does not immediately reduce allocated memory, so it is generally faster.
