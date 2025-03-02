# The time complexity of the reverse implementation of the singly linked list is o(n^2)
1) The function iterates itself from self.get_size()-1 to 0, so it loops n times
2) In each iteration, the pointer traverses the linked list to find the element it needs at position i.

Over the course of the function, the time is then o((n)+(n-1)+(n-2)...(2)+(1)) = o(n^2).

# To optimize the performance of tis code, we need to make sure it doesn't traverse the list multiple times
In this case, after the first iteration, we only need to move from that position.
We do this by having multiple pointers:
next: for forward iteration
current: points to current node being processed 
prev: points to previous node
But this time, we keep changing the pointers so head ends up pointing to the last element,
current to previous, curr.next of the last iteration becomes current of the succeeding iteration. 

The final prev becomes the head, since current can't be None for the next iteration.

This leads to a complexity of o(n) since each loop is a fixed number of constant times.
