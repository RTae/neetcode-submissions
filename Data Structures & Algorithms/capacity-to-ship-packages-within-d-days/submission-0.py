class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the idea is we can look a problem into a upper bound and lower bound of the ship capcity
        # we look at the problem as a capacity instead of days because it's easier
        # so we need to serach the minimim capacity of the ship between lower and upper bound
        # also it should meet the number of days too (or ships)
        # ex. 1,2,3,4,5, capacity should be between [5, 15]

        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap: int):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            
            return ships <= days

        while l <= r:
            cap = (l+r)//2

            if canShip(cap):
                res = min(res, cap)
                r = cap-1
            else :
                l = cap+1
        
        return res