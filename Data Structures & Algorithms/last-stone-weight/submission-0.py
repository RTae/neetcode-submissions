class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stone) > 1:
            first = heaq.heappop(stones)
            second = heaq.heappop(stones)
            if first > second:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])