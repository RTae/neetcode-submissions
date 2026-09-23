class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Using backtracing method to create all possible subset

        res = 0

        def bt(i, subset):
            nonlocal res

            # First we need to sum each subset
            sum_xor = 0
            for num in subset:
                sum_xor^=num
            res+=sum_xor

            # create a subset
            # ex [3,1,1]
            for j in range(i, len(nums)):
                # add new value to create a subset
                # [] -> [3]
                subset.append(nums[j])
                # create the subset of the array
                # [3] with [1,1]
                bt(j+1, subset)
                # remove end to consider another case
                subset.pop()

        # using topdown approch
        bt(0, [])
        return res