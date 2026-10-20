class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the idea is we can group a data into a sequece from a list
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if the nunber is the stat of a sequece
            length = 0
            if (n-1) not in numSet:
                # keep add one until the nunber is not in the set
                while (n+length) in numSet:
                    length += 1
                # check the length of the count
                longest = max(length, longest)
        return longest