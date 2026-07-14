class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevV = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevV:
                return [prevV[diff], i]
            prevV[n] = i