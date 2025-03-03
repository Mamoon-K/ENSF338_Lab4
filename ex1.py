import timeit
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def getData(self):
        return self.__value

    def setData(self, value):
        self.__value = value

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def __str__(self):
        return f'Node Value: {self.__value} Next Node: ({self.__next})'
    
class LinkedList:
    def __init__(self, head):
        self.__head = head
    
    def getHead(self):
        return self.__head
    
    def setHead(self, head):
        self.__head = head

    def headInsert(self, value):
        newNode = Node(value)
        newNode.setNext(self.getHead())

        self.setHead(newNode)

    # Find the middle using the Tortoise and Hare approach shown in the given documentation
    def middle(self, start, last):
        if start is None:
            return None

        if start == last:
            return start

        slow = start
        fast = start.getNext()

        while fast != last:
            fast = fast.getNext()
            slow = slow.getNext()
            if fast != last:
                fast = fast.getNext()

        return slow

    def binary_search(self, num):
        start = self.getHead()
        last = None

        while start != last:  # Prevents infinite loop

            # Find middle
            mid = self.middle(start, last)

            # If middle is empty
            if mid is None:
                return None

            # If value is present at middle
            if mid.getData() == num:
                return mid

            # If value is greater than mid
            elif mid.getData() < num:
                start = mid.getNext()

            # If value is less than mid
            else:
                last = mid

        return None  # Value not found

class Array:
    def __init__(self):
        self.__arr = []

    def set(self, value, index):
        self.__arr[index] = value

    def get(self, index):
        return self.__arr[index]

    def append(self, number):
        self.__arr.append(number)

    def binary_search(self, num):
        low = 0
        high = len(self.__arr) - 1
        while (low <= high):
            mid = (low + high) // 2
            if (num < self.__arr[mid]):
                high = mid - 1
            elif (num > self.__arr[mid]):
                low = mid + 1
            else:
                return mid
        
        return -1

# Question 4 Answer
"""
The complexity of binary search in a linked list is O(n). This is due to the fact that finding the middle element of a given linked list requires
traversing the linked list. This action takes O(n) time compared to O(1) for an array which has the advantage of indexing. Since O(n) is a larger time 
complexity than O(log(n)) it takes precedence here and results in the overall complexity being O(n).
"""

linkedListTimes1000 = []
linkedListTimes2000 = []
linkedListTimes4000 = []
linkedListTimes8000 = []
arrayTimes1000 = []
arrayTimes2000 = []
arrayTimes4000 = []
arrayTimes8000 = []

# We generate a list for each range of input sizes and generate 100 random numbers to test both the array and linked list with the same values
randNums1000 = random.sample(range(1, 1001), 100)
randNums2000 = random.sample(range(1000, 2001), 100)
randNums4000 = random.sample(range(2000, 4001), 100)
randNums8000 = random.sample(range(4000, 8001), 100)
# Test linked list for lists of sizes 1000, 2000, 4000, and 8000
linkedLists = []
for i in [1, 2, 4, 8]:
    headNode = Node(0)
    myList = LinkedList(headNode)
    for j in range(1, (i * 1000) + 1):
        myList.headInsert(j)

    linkedLists.append(myList)

for num in randNums1000:
    linkedListTimes1000.append(timeit.timeit(lambda: linkedLists[0].binary_search(num), number=100) / 100)

for num in randNums2000:
    linkedListTimes2000.append(timeit.timeit(lambda: linkedLists[1].binary_search(num), number=100) / 100)  

for num in randNums4000:
    linkedListTimes4000.append(timeit.timeit(lambda: linkedLists[2].binary_search(num), number=100) / 100)

for num in randNums8000:
    linkedListTimes8000.append(timeit.timeit(lambda: linkedLists[3].binary_search(num), number=100) / 100)

# Get the average time for 1000, 2000, 4000, and 8000
avg1000TimeLists = sum(linkedListTimes1000) / len(linkedListTimes1000)
avg2000TimeLists = sum(linkedListTimes2000) / len(linkedListTimes2000)
avg4000TimeLists = sum(linkedListTimes4000) / len(linkedListTimes4000)
avg8000TimeLists = sum(linkedListTimes8000) / len(linkedListTimes8000)

timesLists = [avg1000TimeLists, avg2000TimeLists, avg4000TimeLists, avg8000TimeLists]
inputVals = [1000, 2000, 4000, 8000]

def linear(x, a, b):
    return a * x + b  # Linear fit

# Fit the curve
params, covariance = curve_fit(linear, inputVals, timesLists)

predicted_y_lists = linear(np.array(inputVals), *params)

# Test arrays for lists of sizes 1000, 2000, 4000, and 8000
arrays = []
for i in [1, 2, 4, 8]:
    arr = Array()
    for j in range(1, (i * 1000) + 1):
        arr.append(j)

    arrays.append(arr)

for num in randNums1000:
    arrayTimes1000.append(timeit.timeit(lambda: arrays[0].binary_search(num), number=100) / 100)

for num in randNums2000:
    arrayTimes2000.append(timeit.timeit(lambda: arrays[1].binary_search(num), number=100) / 100)  

for num in randNums4000:
    arrayTimes4000.append(timeit.timeit(lambda: arrays[2].binary_search(num), number=100) / 100)

for num in randNums8000:
    arrayTimes8000.append(timeit.timeit(lambda: arrays[3].binary_search(num), number=100) / 100)

# Get the average time for 1000, 2000, 4000, and 8000
avg1000TimeArrays = sum(arrayTimes1000) / len(arrayTimes1000)
avg2000TimeArrays = sum(arrayTimes2000) / len(arrayTimes2000)
avg4000TimeArrays = sum(arrayTimes4000) / len(arrayTimes4000)
avg8000TimeArrays = sum(arrayTimes8000) / len(arrayTimes8000)

timesArrays = [avg1000TimeArrays, avg2000TimeArrays, avg4000TimeArrays, avg8000TimeArrays]

# Define a logarithmic function
def logarithmic(x, a, b):
    return a * np.log(x) + b  # Logarithmic fit 

# Fit the curve
params2, covariance2 = curve_fit(logarithmic, inputVals, timesArrays)

# Predict y values using the fitted parameters
predicted_y_arrays = logarithmic(np.array(inputVals), *params2)

plt.figure(figsize=(12, 5))
plt.scatter(inputVals, timesLists, s=10, label="Linked List", color="orange")
plt.scatter(inputVals, timesArrays, s=10, label="Array", color="purple")
plt.plot(inputVals, predicted_y_lists, linestyle="--", label="Linked List Linear Fit", color="blue")
plt.plot(inputVals, predicted_y_arrays, linestyle="--", label="Array Logarithmic Fit", color="red")
plt.xlabel("Input Numbers")
plt.ylabel("Times to find using binary search (s)")
plt.title("Linked List vs Array Times for Binary Search at Various Input Sizes")
plt.legend()
plt.grid()

plt.show()