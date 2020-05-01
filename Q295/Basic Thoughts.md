### Question 295: Find Median from Data Stream
```
This problem has tag "heap", which means we need to use heapify methods to solve the problem
```

##### Heap:
* Heap is a data structure which does _not_ fully sort the list
* the advantage of heap is that we can retrieve the max or min from a heapified list in O(1)

##### Median:
The median number of a list can be calculated by using 1 or 2 numbers in the middle of a sorted list. As a result, the problem we want to deal with is to keep track of the middle numbers when new numbers inserted. 
  
###### Base case(the first two numbers inserted):
we can easily store the first and the second numbers in a list and return one or average of the two as the answer.

###### Recursive case:
* Before the forth numbers inserted into the list, we can put all numbers less than median into a max-heap, which returns the largest number in constant time. Correspondingly, we put all numbers greater than median into a min-heap, which returns the minimum number in constant time.
* When new numbers inserted in odd case (length of the list is an odd number before insertion), first determine which heap the new number belongs to. After that, insert the number into the corresponding heap, re-heapify the heap and pop the corresponding maximum/minimum to median list.
* When new numbers inserted in even case (length of the list is an even number before insertion), first determine which heap the new number belongs to. After that, pop the smaller/larger number of the median list into the corresponding heap.
