import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict()

        for num in nums:
            map[num] = 1 + map.get(num,0)
        heap = []
        for num in map.keys():
            heapq.heappush(heap, (map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        
        return res
