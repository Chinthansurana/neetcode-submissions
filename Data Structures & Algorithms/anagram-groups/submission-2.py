class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for ele in strs:
            i = ''.join(sorted(ele))
            res[i].append(ele)
        return [elem for _, elem in res.items()]