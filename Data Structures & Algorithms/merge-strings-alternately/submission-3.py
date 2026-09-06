class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointer and then apply another string togather
        word1_arr = [c for c in word1]
        word2_arr = [c for c in word2]

        res = ""
        
        while len(word1_arr) != 0 and len(word2_arr) != 0:
            c1 = word1_arr.pop(0)
            c2 = word2_arr.pop(0)
            res+=(c1+c2)
        
        res += "".join(word1_arr) + "".join(word2_arr)
        return res