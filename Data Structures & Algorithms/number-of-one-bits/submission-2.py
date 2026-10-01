class Solution:
    def hammingWeight(self, n: int) -> int:
        # the idea is we can use a bit mask to count only by using n & (n - 1)
        # when we do this we will skip bit 0
        # example
        #  n = 1001, n-1 = 1000, n & n-1 = 1000, count 1
        #  n = 1000, n-1 = 0111, n & n-1 = 0000, count 1
        # so we count only two times
        res = 0
        while n:
            n &= n-1
            res+=1
        
        return res