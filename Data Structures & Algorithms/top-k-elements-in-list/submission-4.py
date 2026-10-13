class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_count = defaultdict(int)

        for n in nums:
            map_count[n]+=1
        
        res = dict(sorted(map_count.items(), key=lambda item: item[1], reverse=True))
        res = list(res.keys())

        return res[:k]