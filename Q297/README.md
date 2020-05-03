### Q297. Serialize and Deserialize Binary Tree
```
We can simply use the idea of BFS and DFS: use BFS to serialize and use DFS to deserialze
```

##### Own algorithm:
###### Serialize:
Use a queue to make sure all the nodes in the tree are visited. If the content in queue are all None, then we know that it is the end of the search.

###### Deserialize:
Use recursive functions that is similar to DFS to go through the list and recreating the nodes one by one. 

##### Attempting methods to imporve efficiency:
* List comprehension (Cannot apply)
* Change the DFS used in previous case to BFS (Increasing compile time from 112ms to 188ms)
