class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        l,r = 0,len(nums)-1
        res= []
        for i,num in enumerate(nums):
            l,r = i+1,len(nums)-1
            if i>0 and num == nums[i-1]:
                continue
            while (l<r):
                total = num + nums[l] + nums[r]
                if (total==0):
                   res.append([num,nums[l],nums[r]]) 
                   l+=1
                   r-=1

                   while (nums[l] == nums[l-1] and l<r):
                    l+=1
                elif (total < 0):
                    l+=1
                else:
                    r-=1
        return res

