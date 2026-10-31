class Solution:
    def myPow(self, x: float, n: int) -> float:
        # the idea is we will use divice and conquer to solve a sub-problem
        # we now that the power of x by n is a x time n times
        # ex. 2^6 is 2*2*2*2*2*2
        # so we can just break a problem into 2^3 * 2^3
        # and solve a problem and so on

        def helper(x, n):
            # some assert to stop
            if x == 0: return 0
            # this help to stop a recursive when we keep n // 2
            if n == 0: return 1

            # we break a problem into sub problem and so on
            res = helper(x*x, n//2)
            # however we need to check id n is odd or even
            # if n is even we can just throw a res
            # if n is odd we can just throw a res*x
            # eg. n=5 it's a 2*2^2*2^2
            return x * res if n % 2 else res 

        res = helper(x, abs(n))

        return res if n>=0 else 1 / res