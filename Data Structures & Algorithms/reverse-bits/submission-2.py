class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Extract current bit
            bit = (n >> i) & 1
            # shift bit to position 31-i
            res += (bit << (31 - i))
        return res