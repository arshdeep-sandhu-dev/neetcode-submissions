class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        
        for index,number in enumerate(nums):
            if target-number in s:
                return [s[target-number],index]
            else:
                s[number]=index
        return [-1,-1]