class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # We need to pay 5 first to keep reduce bill 5
        # if we don't have 5 left mean we cannot pay

        # track bill 5 and 10

        b5, b10 = 0,0
        for b in bills:
            # no need for giving a change
            if b==5:
                b5+=1
            # get 10 bill
            elif b==10:
                b5-=1
                b10+=1
            # get 20 bill, pay with b10
            elif b10 > 0:
                b10-=1
                b5-=1
            # get 20 bill, but don't have b10
            else:
                b5-=3
            
            # mean cannot pay anything
            if b5 < 0:
                return False

        # mean no bill left
        return True