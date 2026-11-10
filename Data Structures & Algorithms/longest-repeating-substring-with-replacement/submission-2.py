class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the idea is to create a table that count the nunber of char
        # then we compare we a current string that if the diff is not than k
        # the length of that substring is the longest
        # we can use sliding window with a char count to check

        res = 0
        # first we need a variable to count check base on what char we want to change
        char_set = set(s)

        for c in char_set:
            count = l = 0

            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                
                # if the lenght of substring more than k in that char count
                # it's mean we require more k char to change that sub-string which is 
                # not qualify our case, so we do a left shift to continue a search
                while r-l+1 - count > k:
                    # then start do a left shift
                    if s[l]==c:
                        count-=1
                    l+=1
            
                res = max(res, r-l+1)
        return res
