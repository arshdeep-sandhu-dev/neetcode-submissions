class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        d = Counter(nums)
        res = 0
        curr = 1
        s =set(nums)
        s = list(s)
        s.append(math.inf)
        s.sort()
        for num in s:
            if num-1 in d:
                curr+=1
            else:
                curr=1
            res = max(res,curr)
        return min(res, len(nums)) 