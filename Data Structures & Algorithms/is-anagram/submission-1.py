class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for sT in s:
            if sT in countS:
                countS[sT]+=1
        
        for tT in t:
            if tT in countT:
                countT[tT]+=1
        
        return countS == countT