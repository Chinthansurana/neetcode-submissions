class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for ele in strs:
            ana = ''.join(sorted(ele))
            anaMap[ana].append(ele)
        return list(anaMap.values())