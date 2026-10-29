class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = k % len(nums)

        nums[:]=nums[-m:]+nums[:-m]