class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Using backtracking method to track all possible subset

        res = 0

        def bt(i, subset):
            nonlocal res
            
            xorr = 0
            for num in subset:
                xorr ^= num
            res += xorr

            # create all possible subset
            # using i as a shifter to keep track which range to process
            for j in range(i, len(nums)):
                subset.append(nums[j])
                # when create this set need to move pointer toward
                bt(j+1, subset)
                subset.pop()

        bt(0, [])

        return res