class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupings = defaultdict(list)

        for string in strs:
            sorted_s = ''.join(sorted(string)) #create sorted string to use as key (e.g. 'act')
            groupings[sorted_s].append(string) 
        
        return list(groupings.values())
