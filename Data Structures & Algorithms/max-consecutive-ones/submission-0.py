class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_window = 0
        count = 0
        m = 0
        for i in nums:
            # start track
            if i == 1 and m == 0:
                m = 1
            # start count
            if i == 1 and m == 1:
                count+=1
            # reset
            if i == 0 and m == 1:
                max_window = max(max_window, count)
                count = 0
                m = 0
        return max(max_window, count)