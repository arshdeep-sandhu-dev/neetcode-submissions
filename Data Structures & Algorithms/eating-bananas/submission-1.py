class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = max(piles)
        l=1
        res=-1
        while l<=most:
            mid =  (l+most)//2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(float(piles[i])/mid)
            if hours<=h:
                res = mid
                most = mid-1
            else:
                l = mid+1
        return res
