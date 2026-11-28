class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the idea is we can look a problem into a upper bound and lower bound of the ship capcity
        # we look at the problem as a capacity instead of days because it's easier
        # so we need to serach the minimim capacity of the ship between lower and upper bound
        # also it should meet the number of days too (or ships)
        # ex. 1,2,3,4,5, capacity should be between [5, 15]
        # possible value are 9 and 11, but the answer we want is 9

        # first set a search range between min and mac capacity of the ship 
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap: int):
            # we set a counter for number of ship and cap to check is it possible to ship
            ships, currCap = 1, cap
            # we loop every possible weights
            for w in weights:
                # check that the weight is not exceed quota of the ship's capacity 
                # then increase ship counter and reset counter for a new ship
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                # remove weight
                currCap -= w
            
            return ships <= days

        # do like a normal binary serach and using cap as a search value
        while l <= r:
            cap = (l+r)//2

            if canShip(cap):
                res = min(res, cap)
                r = cap-1
            else :
                l = cap+1
        
        return res