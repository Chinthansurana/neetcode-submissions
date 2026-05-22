class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            ele = ''.join(sorted(i))
            res[ele].append(i)
        return [ele for ele in res.values()]