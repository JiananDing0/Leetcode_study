### Question 274: H-Index
```
This is a very interesting dynamic programming problem
```
  
  
Some information we can easily figure out:
* The upper bound of value h is N, the length of the input array
* The lower bound of value h is 0, which is true when the array is composed of all 0's or the array is empty.

**Hint: Consider it as a dynamic programming problem, if we start from the end of the array, what should be the value of h each time?**
For example, array ```0, 1, 3, 5, 6```:
1. when the array is ```6```, value of h should be 1.
2. when the array is ```5, 6```, value of h should be 2.
3. when the array is ```3, 5, 6```, value of h should be 3.
...
