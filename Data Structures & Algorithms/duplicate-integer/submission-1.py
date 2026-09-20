class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash:
                return False
            hash[num] = 1