class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftsum
            if leftsum == rightSum:
                return i
            
            leftsum += nums[i]
        
        return -1