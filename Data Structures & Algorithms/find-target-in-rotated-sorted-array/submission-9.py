class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums)-1

        while (l<=r):
            m = l + (r-l)//2
            left = nums[l]
            right = nums[r]
            middle = nums[m]
            if (target == middle):
                return m
            if ( left <= middle):
                if target > middle or target < left:
                    l = m+1
                else:
                    r = m-1
                    
            else:
                if (target < middle) or target> right:
                    r = m -1
                else:
                    l = m+1
        return -1


