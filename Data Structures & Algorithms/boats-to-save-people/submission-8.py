class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        boat=0
        l,r=0,len(people)-1

        while l<=r:
            remaining=limit-people[r]
            r-=1
            boat+=1

            if remaining >= people[l] and l<=r:
                l+=1
        return boat