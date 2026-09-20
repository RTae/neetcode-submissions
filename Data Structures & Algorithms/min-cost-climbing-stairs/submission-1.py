class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if cache[i] != 101:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]

        return dfs(0)