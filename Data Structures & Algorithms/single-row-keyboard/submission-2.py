class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # convert keyboard into index first
        # then we do a map, so we can reduce a loop for keyboard

        keyboard_map = {}

        for idx, k in enumerate(keyboard):
            keyboard_map[k] = idx
        
        res = 0
        cur_idx = 0
        for w in word:
            # cal distant
            res += abs(cur_idx - keyboard_map[w])
            # move index to current char
            cur_idx = keyboard_map[w]           


        return res