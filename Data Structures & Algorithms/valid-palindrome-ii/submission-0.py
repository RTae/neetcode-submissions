class Solution:
    def validPalindrome(self, s: str) -> bool:
        # using two pointer method
        # since this probelm 

        def is_parlindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
    
        l,r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return is_parlindrome(l+1,r) or is_parlindrome(l,r-1)
            
            l += 1
            r -= 1

        return True