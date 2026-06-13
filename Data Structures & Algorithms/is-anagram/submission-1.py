class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d2={}
        for letter in s:
            if letter not in d:
                d[letter]=0
            else:
                d[letter]+=1
        for letter in t:
            if letter not in d2:
                d2[letter]=0
            else:
                d2[letter]+=1
        if d == d2:
            return True
        else:
            return False
        
        