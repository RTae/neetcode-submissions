class Solution:
    def mySqrt(self, x: int) -> int:
        # Apply a binaray search to find a sqrt value of line x number
        # ex 9
        # 1 2 3 4 5 6 7 8 9
        # since sqrt is a y*y value to equal x
        # so we find it by check the center of line x and then return lower bound
        # 5 * 5 > 9, so shift right => 1 2 3 4
        # 3*3 == 9: retun 3
        # if number cannot be squt return lower bound


        l, r = 0, x
        res = 0
        while l <= r:
            # we find it by check the center of line x and then return lower bound
            m = l + (r-l)//2
            # since sqrt is a y*y value to equal x
            if m*m > x:
                r = m - 1
            # if target value lower than center value, so keep that res as a lower bound
            # and keep finding unti there is no line number to search
            elif m*m < x:
                l = m + 1
                res = m
            # it's a value
            else:
                return m
        
        return res