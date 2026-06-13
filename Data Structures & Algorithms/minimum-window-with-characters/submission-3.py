class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or len(t)==0:
            return ""
        dt = Counter(t)

        ds = defaultdict(int)
        need = len(dt)
        start = 0
        end = len(s)+1
        have = 0
        l=0
        for r,letter in enumerate(s):
            ds[letter] +=1
            if (ds[letter] == dt[letter]):
                have+=1
            while have == need:
                if (end-start > r-l+1):
                    start = l
                    end = r+1
                ds[s[l]]-=1
                if ( s[l] in dt and ds[s[l]] < dt[s[l]]):
                    have -=1
                l+=1
        print(end)
        return "" if (len(s)+1==end) else s[start:end]
