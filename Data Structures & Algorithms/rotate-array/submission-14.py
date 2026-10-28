class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we can a split point at k
        m = k % len(nums)
        # then we move from -m: (move from m from back) to front and move :-m to back (move from m count from the back)
        # [1,2,3,4,5] k=3
        # m=3
        # num[-m:]=[3,4,5]
        # num[:-m]=[1,2] 
        nums[:] = nums[-m:] + nums[:-m]