import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_size(self):
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        return size

    def get_element_at_pos(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp

    # Given O(n²) reverse implementation
    def reverse_slow(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size() - 1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # Optimized O(n) reverse implementation
    def reverse_fast(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

# Function to generate a random linked list of given size
def generate_linked_list(size):
    ll = LinkedList()
    for _ in range(size):
        ll.insert_head(random.randint(1, 1000))
    return ll

# Function to measure execution time
def measure_time(reverse_method, size, runs=100):
    times = timeit.repeat(lambda: reverse_method(), repeat=runs, number=1)
    return sum(times) / runs  # Return average time

# List sizes for testing
sizes = [1000, 2000, 3000, 4000]

# Run benchmarks
results = {"slow": [], "fast": []}

for size in sizes:
    print(f"Testing list size {size}...")

    ll_slow = generate_linked_list(size)  # Generate a new list for each test
    ll_fast = LinkedList()  # Copy elements to a new list
    temp = ll_slow.head
    while temp:
        ll_fast.insert_head(temp.data)
        temp = temp.next

    # Measure both implementations
    time_slow = measure_time(ll_slow.reverse_slow, size)
    time_fast = measure_time(ll_fast.reverse_fast, size)

    results["slow"].append(time_slow)
    results["fast"].append(time_fast)

    print(f"Slow (O(n²)) time: {time_slow:.6f} sec")
    print(f"Fast (O(n)) time: {time_fast:.6f} sec\n")

# Save results for plotting
import matplotlib.pyplot as plt

plt.plot(sizes, results["slow"], label="O(n²) Reverse", marker="o", linestyle="--")
plt.plot(sizes, results["fast"], label="O(n) Reverse", marker="o", linestyle="-")
plt.xlabel("List Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Reverse Linked List")
plt.legend()
plt.grid()
plt.show()
