class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # using two pointer concept
        # find a max area by moving a left or right by check which column is lower move that
        # becaue to maxize are we need to find a column that almost same size and far apart
        l,r = 0, len(heights)-1
        res = 0
        while l < r:
            area = min(heights[l], heights[r])*(r-l)
            res = max(res, area)
            
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return res