class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # using two pointer concept
        # find a max area by moving a left or right by check which column is lower move that
        # becaue to maxize are we need to find a column that almost same size and far apart

        l, r = 0, len(heights)-1
        res = 0

        while l < r:
            # we need to select a column a short column, since it can hold a water
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)

            # we need to left or right by which side of column is lower
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return res