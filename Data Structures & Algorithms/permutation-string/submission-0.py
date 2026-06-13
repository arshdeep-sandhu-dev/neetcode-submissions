class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1 = Counter(s1)
        ds2 = defaultdict(int)
        l=0
        for r,letter in enumerate(s2):

            if (r-l+1 > len(s1)):
                ds2[s2[l]]-=1
                if ds2[s2[l]]==0:
                    ds2.pop(s2[l])
                l+=1
                
            ds2[letter]+=1
            print(ds2)
            print(ds1)
            print()
            if (ds2 ==ds1):
                return True
            
        
        return False

            
