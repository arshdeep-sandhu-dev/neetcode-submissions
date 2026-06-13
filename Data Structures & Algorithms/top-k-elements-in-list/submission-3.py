class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        counts = Counter(nums)
        print(counts)
        for key,value in counts.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for key,value in heap:
            res.append(value)
        return res