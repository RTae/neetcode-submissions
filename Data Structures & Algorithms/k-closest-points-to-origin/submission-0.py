class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [ math.sqrt(0-point[0])**2 + math.sqrt(0-point[1])**2 for point in points]
        maxHeap = []
        for x,y in points:
            dist = -(x**2 + y**2)
            heapq.heapush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappush(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])

        return res  