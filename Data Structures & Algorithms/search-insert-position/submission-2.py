class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search 

        l, r = 0, len(nums)
        while l < r:
            m = l + ((r-l) //2)
            if nums[m] >= target:
                r=m
            elif nums[m] < target:
                l=m
        return l 