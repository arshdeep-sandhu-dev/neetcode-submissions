class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0,len(height)-1
        maxL,maxR = height[0], height[r]
        totalArea = 0
        while l<r:
            print(height[l],height[r], totalArea)
            if maxL < maxR:
                l+=1
                maxL = max(maxL,height[l])
                
                totalArea += max(0,(maxL-height[l]))
            else:
                r-=1
                maxR = max(maxR,height[r])
                
                totalArea += max(0,(maxR-height[r]))
        return totalArea

            