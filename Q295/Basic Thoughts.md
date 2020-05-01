### Question 295: Find Median from Data Stream
```
This problem has tag "heap", which means we need to use heapify methods to solve the problem
```

##### Heap:
* Heap is a data structure which does *not* fully sort the list
* the advantage of heap is that we can retrieve the max or min from a heapified list in O(1)

##### Median:
The median number of a list can be calculated by using 1 or 2 numbers in the middle of a sorted list. As a result, the problem we want to deal with is to keep track of the middle numbers when new numbers inserted. 
  
###### Base case(the first two numbers inserted):
