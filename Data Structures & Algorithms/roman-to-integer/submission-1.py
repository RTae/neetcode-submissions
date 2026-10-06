class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        res = 0
        for i in range(len(s)):
            # if i char value less than i+1 char value then do a minus
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            # if more than do a plus
            else:
                res += roman[s[i]]

        return res