class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # apply binary search 
        l, r = 0, len(nums)
        while l < r:
            # create a center check, since it's sorted array
            m = l + ((r - l) // 2)
            # if data at m less than target we need to shift right
            if nums[m] >= target:
                r = m
            # if data at m more than target we need to shift left
            elif nums[m] < target:
                l = m + 1
        return l