class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        times = sorted([(p,s) for p,s in zip(position,speed)])
        total_fleets = 0
        stack = []
        for p,s in times[::-1]:
            time = (target-p)/s

            if not stack or (stack and time > stack[-1]):
                stack.append(time)
            

            

        return len(stack)