class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)//2
        freq = Counter(nums)
        for ele, val in freq.items():
            if val > maj:
                return ele
        return 