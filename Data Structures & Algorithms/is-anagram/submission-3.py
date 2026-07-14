class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for sT, tT in zip(s,t):
            if sT not in countS:
                countS[sT] = 1
            if tT not in countT:
                countT[tT] = 1
            
            countS[sT]+=1
            countT[tT]+=1
        
        return countS == countT