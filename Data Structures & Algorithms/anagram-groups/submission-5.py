class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []

        for s in strs:
            count = [0] * 26
            for c in s:
                pos = ord('a') - ord(c)
                count[pos] += 1
            
            groups[tuple(count)].append(s)

        for group in groups.values():
            res.append(group)

        return res