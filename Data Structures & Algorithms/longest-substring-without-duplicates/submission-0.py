class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        d=set()
        length=0
        while r<len(s):
            letter=s[r]
            while letter in d:
                d.remove(s[l])
                l+=1
            length=max(length,r-l+1)
            d.add(letter)
            r+=1
        return length
            