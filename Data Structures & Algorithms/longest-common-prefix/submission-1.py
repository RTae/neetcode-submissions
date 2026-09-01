class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the idea is we loop check each one by one
        
        # first we need a reference first
        prefix = strs[0]
        # check word by word
        for i in range(1, len(strs)):
            j = 0
            # the idea is the j that loop is char should less than prefix or length of that stars[i]
            # example if prefix is flow and strs[i] is fop the length j should go is 3, since we don't care after that
            while j < min(len(prefix), len(strs[i])):
                # if check until is not a same
                if prefix[j] != strs[i][j]:
                    break                
                j+=1
            # trip it
            prefix=prefix[:j]
        return prefix