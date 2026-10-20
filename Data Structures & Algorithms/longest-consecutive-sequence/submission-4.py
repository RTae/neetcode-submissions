class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the idea is we can group a data into a sequence from a list
        # example : 12, 132, 1, 232, 2,32, 2321,3
        # if we group a data into a each sequence we will get
        # 1,2,3 12, 32, 132, 2321
        # from this we can see here that the length is just a sequence length from nums
        # we can loop and keep add 1 and check the next value is in the nun set or not
        # if not just stop the loop
        # then return a result

        # check the length
        numSet = set(nums)
        # keep track longest 
        longest = 0

        for n in nums:
            # n-1 is for helping not to count same nunber twice
            # to star each count
            if (n-1) not in numSet:
                length = 1
                # loop until we cannot a find a number in that set
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest