class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = {}
        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            if (r - l + 1) - max(counts.values()) <= k:
                res = max(res, (r - l + 1))
            else:
                counts[s[l]] -= 1
                l += 1

        return res