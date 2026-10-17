class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x:x[0])
        res:list[list[int]] = [intervals[0]]
        
        for start, end in intervals[1:]:
            prevend = res[-1][1]
            if prevend >= start:
                res[-1][1] = max(prevend, end)
            else:
                res.append([start, end])
        return res
