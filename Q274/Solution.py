class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Sort
        citations = sorted(citations)
        # Dynamic programming
        hIndex = 0
        for i in range(1, len(citations) + 1):
            if hIndex < citations[-i]:
                hIndex = i
        return hIndex
