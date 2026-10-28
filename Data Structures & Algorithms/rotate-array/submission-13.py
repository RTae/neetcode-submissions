class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We split the array into two blocks: the last m elements (which move
        # to the front) and the rest (which shift to the back).
        #
        # Example: nums = [1,2,3,4,5,6,7,8], k = 4  ->  m = 4 % 8 = 4
        #
        #   nums[-m:]  = nums[-4:] = [5,6,7,8]   <- last m, moves to front
        #   nums[:-m]  = nums[:-4] = [1,2,3,4]   <- the rest, shifts back
        #
        #   nums[:] = [5,6,7,8] + [1,2,3,4] = [5,6,7,8,1,2,3,4]
        #
        # Why the minus? A negative index counts from the END of the list:
        #   nums[-m:]  -> start m positions from the end, go to the end
        #   nums[:-m]  -> everything up to but NOT including the last m
        # Without the minus, nums[m:] would grab the wrong slice for most k
        # (e.g. k=2: nums[-2:] = [7,8], but nums[2:] = [3,4,5,6,7,8]).
        #
        # k % len(nums) handles k >= n (full rotations cancel out).
        # nums[:] = ... mutates in place so the caller sees the change.
        m = k % len(nums)
        nums[:] = nums[-m:] + nums[:-m]