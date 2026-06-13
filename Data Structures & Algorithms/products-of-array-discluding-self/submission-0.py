class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1

        pre = []

        for num in nums:
            pre.append(prefix)
            prefix*=num
        for i,num in enumerate(nums[::-1]):
            pre[len(nums)-1-i]*=postfix
            postfix*=num
        return pre