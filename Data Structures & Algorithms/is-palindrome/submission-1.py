class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointer method

        # remove space and specical string first
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()

        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True