### Question 11: Container with most water
```
Brute force method in this problem seems to be redundant. Can try sliding window solution
```

The theory of this problem is that if you move the longer side inwards, then the area must be decreasing because the area is _*always*_ be determined by the _*shorter side*_. Based on idea of greedy, we should always move the shorter side inwards in order to keep the area have some possibilites to become better and we must be able to go through the best answer in this process.
