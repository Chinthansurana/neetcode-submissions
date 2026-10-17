class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        res:list[list[int]] = [intervals[0][:]]
        cnt:int = 0
        for start, end in intervals[1:]:
            prevend = res[-1][1]
            if prevend > start:
                cnt += 1
            else:
                res.append([start, end])
        return cnt