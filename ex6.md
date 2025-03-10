## Ex 6.1
Some advantages to an array over a linked list are the constant time (O(1)) complexity of accessing elements by index.
 This is better than a linked list where accessing elements is O(n) complexity since it must traverse the list to find the correct element.
  However, insertion and deletion in an array is of O(n) complexity since you must shift elements to insert or delete another element 
  unless the element is at the end. This means that in the worst case, you would need to go over every element to shift them and insert/delete
   leading to the O(n) complexity. On the other hand, for linked lists if you insert and delete at its head, 
   that is O(1) complexity since you always add or remove the item at the same position and you do not have to move any other nodes
    excluding the pointers stored in potentially one other node. If you insert or delete at other locations in the linked list however, 
    it is similar to an array at O(n) complexity since you need to traverse the list to find where you want to insert/delete.

## Ex 6.2
In an array, to replace a value using deletion and then insertion, you can copy the value at the end of the array to the position of the value you want to delete,
 and then delete the last element of the array. From there, you can insert the new value that you are replacing the old value with at the end of the array. 
 This will help to minimize the time by inserting and deleting at the end of the array where you do not need to shift elements of the array 
 to expand and contract the size of the array within it's capacity in both insertion and deletion.

## Ex 6.3
It is possible to use both insertion and merge sort in a doubly linked list.
 In terms of insertion sort, it can be done since you can traverse through the current linked list
  and basically insert these into a sorted linked list that starts empty and is filled as you go through the current list.
   This is done by looping through each element of the original list and if the current element does not need to be put at the head,
    then also looping through the sorted list to find where to insert this node. This means that it has a time complexity of O(n^2) in the worst case
     since it will use nested loops or O(n) in the best case where it inserts everything at head. However, due to interfacing with a linked list,
      the implementation is more complicated and longer than the similar array based approach.

Additionally, merge sort can also be used although it is a little more complex to implement.
 You can use the general merge sort function for arrays, but creating split and merge functions that works for a doubly linked list.
  In the split function, you basically must find the middle of the linked list that it is given which can be done using different algorithms. 
  Additionally, for merging you can simply create new lists by making new head values and inserting the nodes in the correct positions by comparing their values.
   This is effectively the same process as for the array merge sort but adapted to search and insert in a linked list.
    Therefore, the algorithm still splits the array in half every level leading to a O(log(n)) complexity for splitting
     and then it simply has to go through all the elements in the linked lists to merge them back
      (since it finds the lesser value between two already individually sorted arrays) so merging has a O(n) complexity.
       Therefore, the overall complexity of the merge sort is still O(nlog(n)) so this is a more feasible algorithm to use.

# Ex 6.4
As explained in ex6.3, the complexities for insertion sort in the worst case is O(n^2) while for merge sort it is O(nlog(n)).
 These are the same complexities as the array versions of these algorithms which makes sense since they are implemented in very similar ways
  with modifications made to interface with the more complex data structure of the linked list. 
  This introduces an overhead since there is more code that is run, however in terms of big O notation where we ignore constant values, 
  this does not change the overall complexity. Hence, the complexities for the linked list versions match those of the array implementations.