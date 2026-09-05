class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Using two pointer method and apply a sub-problem
        
        def is_palindrome(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                # if we found it does not match case we create a sub-problem to keep check it
                return is_palindrome(l+1,r) or is_palindrome(l,r-1)

            l+=1
            r-=1

        return True