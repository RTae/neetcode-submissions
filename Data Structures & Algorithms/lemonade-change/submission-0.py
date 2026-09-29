class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5, bill10 = 0,0
        for b in bills:
            # bill 5
            if b==5:
                bill5+=1
            # bill 10
            elif b==10:
                bill5-=1
                bill10+=1
            # bill 20 and we have 10
            elif bill10 > 0:
                # pay both bill
                bill5-=1
                bill10-=1
            # bill 20 and we don't have 10
            else:
                # pay only 5
                bill5-=3
            
            # we cannot pay after this
            if bill5 < 0:
                return False
            
        return True