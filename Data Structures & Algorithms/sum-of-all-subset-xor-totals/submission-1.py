class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Using backtracking method to create all possible subset

        # result sum
        res = 0
        def backtrack(i, subset):
            nonlocal res

            # tracking sum in each subset
            xorr = 0
            for num in subset:
                xorr ^= num
            
            # sum back to result
            res += xorr

            # create a subset
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()
        
        # start from topdown
        backtrack(0, [])
        return res