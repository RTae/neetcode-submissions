class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # the idea we can use DP to solve this problem by using 2D DP
        # We will use bottom up approch by
        # go diagoanal + 1 if char is same
        # go from right or down if char is not same
        #   C A T
        # C 3 0 0
        # R 2 0 0
        # A 0 1 0
        # B 0 1 0
        # T 0 0 1

        dp = [[ 0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]