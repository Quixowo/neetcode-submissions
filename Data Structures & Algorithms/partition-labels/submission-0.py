class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        res = []
        for i, c in enumerate(s):
            count[c] = i

        end = count[s[0]]
        size = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, count[c])
            if i == end:
                res.append(size)
                size = 0

        return res