class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strList = defaultdict(list)

        for s in strs:
            sorted_word = ''.join(sorted(s))
            
            strList[sorted_word].append(s)

        return list(strList.values())
