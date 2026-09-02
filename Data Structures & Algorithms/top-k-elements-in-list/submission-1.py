class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict()
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            map[num] = 1 + map.get(num,0)
        for num, count in map.items():
            buckets[count].append(num)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if (len(result) == k):
                    return result
        
