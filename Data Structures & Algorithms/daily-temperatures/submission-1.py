class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= []
        res = [0]*len(temperatures)
        for index,temperature in enumerate(temperatures):

            while stack and stack[-1][0] < temperature:
                _ , prevIndex = stack.pop()
                res[prevIndex] = index-prevIndex
            stack.append((temperature,index))
        return res