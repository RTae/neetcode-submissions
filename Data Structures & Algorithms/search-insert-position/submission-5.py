class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Apply a binary search 
        l, r = 0, len(nums)
        while l < r:
            # keep update center of array
            m = l + ((r-l)//2)
            # need to shift right
            if nums[m] >= target:
                r=m
            # need to shift left
            elif nums[m] < target:
                l=m+1
        
        return l