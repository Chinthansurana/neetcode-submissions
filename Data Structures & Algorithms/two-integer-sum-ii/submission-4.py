class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i<j:
            curr = numbers[i] + numbers[j]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return [i+1, j+1]
        return [-1, -1]
        