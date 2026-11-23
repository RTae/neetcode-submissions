class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # the concept is using prefix sum to find a sum from left side
        # and keep subtract from right side

        total = sum(nums)
        leftsum = 0

        for i in range(len(nums)):
            rightsum = total - nums[i] - leftsum

            if rightsum == leftsum:
                return i
            
            leftsum+=nums[i]

        return -1