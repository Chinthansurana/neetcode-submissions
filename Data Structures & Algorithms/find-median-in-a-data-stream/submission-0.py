class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) > len(self.large):
            ele = -heapq.heappop(self.small)
            heapq.heappush(self.large, ele)
        if len(self.large) > len(self.small):
            ele = heapq.heappop(self.large)
            heapq.heappush(self.small, -ele)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        return (-1*(self.small[0]) + self.large[0]) / 2
        
        
        