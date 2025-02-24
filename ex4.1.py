# Given Function from ex4 Lab Slides:

def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[j] *= 2

"""
QUESTION 1:

Best Case Complexity - O(n):
The best case occurs when the if condition li[i] > 5 never evaluates to True for any element.
In this scenario, only the outer loop runs, iterating n times without triggering the inner loop.

Worst Case Complexity - O(n²):
The worst case occurs when the if condition li[i] > 5 is always True for all n elements.
In this case:
The outer loop runs n times.
For each iteration of the outer loop, the inner loop runs O(n) times.
This results in O(n) * O(n) = O(n²) complexity.

Average Case Complexity - O(n²):
The average case depends on how often li[i] > 5 is true.
If ~ half of the elements satisfy li[i] > 5, the inner loop will execute in approximately O(n²/2) = O(n²).
This still results in an O(n²) average complexity.

"""


'''
QUESTION 2:

No, the complexities are not the same originally. 
Modified function to ensure that all complexities are the same, that is, O(n²)
I removed the if statement from the original function.

Now, the outer loop runs n times, and the inner loop runs n times. The best, worst, and average
complexities remain the same, O(n²).
'''

def processdata(li):
    for i in range(len(li)):
        for j in range(len(li)): # Always executes now
            li[j] *= 2


