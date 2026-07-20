class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # there are two way to rob a house
        # 1. rob i house and rob i+2 house, since we cannot rob adjcent house
        # 2. rob i+1 house
        # Then check which case give more money

        # we need to check very possible case of the house number and cache it's cal value
        cache = [-1] * len(nums)

        def dfs(i):
            # exceed number of house
            if i >= len(nums):
                return 0

            # it's already calculate
            if cache[i] != -1:
                return cache[i]

            # Compare between case 1 and 2
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))

            return cache[i]
        
        # start at first house
        return dfs(0)