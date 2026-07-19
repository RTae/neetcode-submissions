class Solution:
    def climbStairs(self, n: int) -> int:
        # add a lookup table for pass value
        cache = [-1]*n
        def dfs(i):
            # we recurive exceed the n
            if i >= n:
                return i == n
            # we there is a value in cahce no need to calcuate just return it
            if cache[i] != -1:
                return cache[i]
            # since we can move 1 and 2 steps, so we need to create a resursive of subproblem and combine it
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)