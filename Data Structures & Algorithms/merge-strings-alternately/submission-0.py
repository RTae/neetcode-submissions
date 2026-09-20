class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_arr = [c for c in word1]
        word2_arr = [c for c in word2]

        res = ""
        
        while len(word1_arr) != 0 and len(word2_arr) != 0:
            c1 = word1_arr.pop()
            c2 = word2_arr.pop()
            res+=(c1+c2)
        
        return res