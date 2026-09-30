class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            # since we need to check whatever there is a sigle number or not. we can use xor to check that by
            # a ^ a = 0
            # a ^ 0 = a # this check to track single value
            res = num ^ res
        
        return res