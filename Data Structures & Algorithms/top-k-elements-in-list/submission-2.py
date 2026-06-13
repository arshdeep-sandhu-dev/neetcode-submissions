class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        news = set(nums)
        
        for number in news:
            list1.append((nums.count(number),number))
        sortedlist = sorted(list1)
        sortedlist[::] = sortedlist[::-1]
        newlist=[]
        for _,number in sortedlist[0:k]:
            newlist.append(number)
        return newlist
