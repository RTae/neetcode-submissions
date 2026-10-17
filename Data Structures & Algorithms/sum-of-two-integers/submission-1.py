class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Using bitwise and bit masking concept to calculate
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b!=0:
            # first and to get a carry and then shift left
            carry = (a & b) << 1
            # then or a or to add and add to mask
            a = (a ^ b) & mask
            # then do a and again to add a carry
            b = carry & mask
        # a <= 0x7FFFFFFF: sign bit is 0, so it's a real positive 32-bit value — return as-is
        # sign bit (bit 31) is set -> a is really negative.
        # a is currently an UNSIGNED 32-bit value (huge positive),
        # so sign-extend it back to a proper Python negative int:
        #   a ^ mask  -> lower 32 bits untouched, ~ -> correct negative
        return a if a <= max_int else ~(a ^ mask)