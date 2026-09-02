class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        for i in range(s_len-1,-1,-1):
            tmp = s.pop(i)
            s.append(tmp)