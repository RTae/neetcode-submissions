class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        curr_idx = 0
        res = 0
        for c in word:
            for k in range(len(keyboard)):
                if c == keyboard[k]:
                    res += abs(curr_idx-k)
                    curr_idx = k
        

        return res