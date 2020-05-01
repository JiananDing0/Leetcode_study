import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = []
        self.size = 0
        self.leftHeap = [] # Max heap for numbers smaller than median
        self.rightHeap = [] # Min heap for numbers smaller than median

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.size += 1
        if self.size == 1:
            self.median.append(num)
        else:
            if self.size % 2 == 1:
                a = min(self.median)
                b = max(self.median)
                if num > max(self.median):
                    heapq.heappush(self.rightHeap, num)
                    heapq.heappush(self.leftHeap, -a)
                    self.median = [b]
                elif num < min(self.median):
                    heapq.heappush(self.leftHeap, -num)
                    heapq.heappush(self.rightHeap, b)
                    self.median = [a]
                else:
                    heapq.heappush(self.leftHeap, -a)
                    heapq.heappush(self.rightHeap, b)
                    self.median = [num]
            elif self.size % 2 == 0:
                if num >= self.median[0]:
                    self.median.append(heapq.heappushpop(self.rightHeap, num))
                elif num < self.median[0]:
                    self.median.append(-heapq.heappushpop(self.leftHeap, -num))              
        return None

    def findMedian(self):
        """
        :rtype: float
        """
        return float(sum(self.median)) / len(self.median)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
