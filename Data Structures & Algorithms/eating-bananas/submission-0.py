class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while (l<=r):
            speed = 0
            m = l + (r-l)//2
            for pile in piles:
                speed += math.ceil(pile/m)
            if ( speed <= h):
                r = m-1
            else:
                l = m+1
        return l

