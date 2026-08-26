class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift = 0
        for dir, amount in shift:
            if dir == 1:
                amount = -amount
            left_shift += amount
        
        # do a left shift and convert to 
        left_shift %= len(s)
        s = s[left_shift:] + s[:left_shift]
        return s