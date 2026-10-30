class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:  
        # the idea is we can use greedy method with two pointer
        # to simplify a problem we can sort it and then chek from hevery poeple to lightweight poeple
        
        people.sort()
        boat=0

        l,r = 0, len(people)-1
        
        while l<=r:
            # we need to put hevery poeple fisrt from greedy concept 
            remaining_weight=limit-people[r]

            r-=1
            boat+=1

            if l<=r and remaining_weight>=people[l]:
                l+=1
        
        return boat