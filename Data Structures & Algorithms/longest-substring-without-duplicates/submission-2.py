class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the idea we can use sliding windown to scan a text to get a longest sub-string

        # to track the string in sub-string to make sure it's not duplicate
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # if there is a duplicate in the sub-string we need to remove and shift pointer left

            # we need to use while not if, since the problem want it to be contiguous
            # so we need to keep we move until it's gone
            # not just remove one times
            # like abccb, second c is dupplicated, so if we use it will remove on a 
            # and let the result be bccb which is wrong even we have another b to move in some case it's can be wrong
            while s[r] in charset:
                # we already pass left pointer for sure, so we can remove from left
                charset.remove(s[l])
                l+=1
            # if our char is not duplicate keep adding
            charset.add(s[r])
            res = max(res, r-l+1)
        
        return res