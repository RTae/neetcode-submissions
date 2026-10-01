class Solution:
    def hammingWeight(self, n: int) -> int:
        # the idea is we can use a bit mask to count only by using n & (n - 1)
        # when we do this we will skip bit 0
        res = 0
        while n:
            n &= n-1
            res+=1
        
        return res