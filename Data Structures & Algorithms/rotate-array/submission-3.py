class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find a middle pointe to separate
        # we need to mod because if k more than lenght of nums
        # so the mid point will loop by carry over
        # like k=3, len(nums)=7, m=3
        # if k=9, len(nums)=7, m=3

        m = k%len(nums)
        nums[:] = nums[-m:]+nums[:-m]