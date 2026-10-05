class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            # the idea is we can use a idea from OXR that same number cancel out, since we try to find a missing number we can use a index as a reference
        n = len(nums)
        xorr = n
        for i in range(n):
            # if we have data like this [0, 2]
            # when we do a xor we get 
            #   0 xor 0 = 0, xorr = 2 xor 0 = 2
            #   1 xor 2 = 1, xorr = 2 xor 1 = 1
            xorr ^= i ^ nums[i]
        # then we will get 1 is missing
        return xorr