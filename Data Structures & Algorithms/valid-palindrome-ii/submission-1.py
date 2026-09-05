class Solution:
    def validPalindrome(self, s: str) -> bool:
        # using two pointer method
        # since this problem require you to also check sub-string is possible to be a palidrome

        # create a function to check normal palidrome
        def is_parlindrome(l,r):
            # keep step from both end
            while l < r:
                # if not same return false
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
    
        l,r = 0, len(s)-1
        # apply same principle, create a sub-problem
        while l < r:
            if s[l] != s[r]:
                return is_parlindrome(l+1,r) or is_parlindrome(l,r-1)
            
            l += 1
            r -= 1

        return True