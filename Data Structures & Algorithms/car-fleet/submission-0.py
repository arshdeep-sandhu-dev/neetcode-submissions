class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        coupled=[(p,s) for p,s in zip(position,speed)]
        coupled.sort()

        res=[]
        time=0
        for p,s in coupled[::-1]:
            res.append((target-p)/s)
            if len(res)>1 and res[-1] <=res[-2]:
                res.pop()
        return len(res)
            
        return len(res)