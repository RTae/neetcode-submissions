class Solution:
    def climbStairs(self, n: int) -> int:
        # the idea is we need to make step 1 and step 2 into a sub problem and then we merge it togather
        # to save up memory we will use cache table to be a look up table
        # we will caclulate every possible n steps
        cache = [-1]*n

        def dfs(i):
            # we recursive exceed target
            if i>=n:
                return i==n
            
            # it mean we already calcuate it, so we can return that value
            if cache[i] != -1:
                return cache[i]

            # we need to combine a subproblem of step 1 and step 2 togather
            cache[i] = dfs(i+1) + dfs(i+2)

            return cache[i]

        # start at zero
        return dfs(0)