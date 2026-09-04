class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use a two pointer from start and end

        # remove all non-alphanumeric characters
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()

        i = 0
        while i <= len(s)-1-i:
            if s[i] != s[len(s)-1-i]:
                return False
            
            i+=1
        
        return True