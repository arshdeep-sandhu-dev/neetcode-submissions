class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        index=0
        
        for word in strs:
            sortedword= "".join(sorted(word))
            
            if sortedword not in d:
                d[sortedword] = [word]
            else:
                d[sortedword].append(word)
        return d.values()