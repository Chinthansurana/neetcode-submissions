class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in strs:
            ele = ''.join(sorted(i))
            hmap[ele].append(i)
        return [res for res in hmap.values()]
        