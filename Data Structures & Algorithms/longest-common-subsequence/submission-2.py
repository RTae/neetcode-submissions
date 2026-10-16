class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom-up DP. dp[i][j] = LCS length of text1[i:] and text2[j:]
        # We fill from bottom-right to top-left so that when computing dp[i][j],
        # the cells we depend on (dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
        # are ALREADY computed.
        #
        # Transition:
        #   text1[i] == text2[j]  ->  1 + dp[i+1][j+1]   (take the diag, keep both chars)
        #   text1[i] != text2[j]  ->  max(dp[i][j+1],   (skip text2[j])
        #                                 dp[i+1][j])   (skip text1[i])
        #
        # Example: text1 = "cat", text2 = "crabt"
        #
        #      c  r  a  b  t  |
        #  c   3  2  2  1  1  | 0
        #  a   2  2  2  1  1  | 0
        #  t   1  1  1  1  1  | 0
        # --------------------+
        #      0  0  0  0  0  | 0
        #
        # Walk through a couple of cells:
        #   dp[2][4]: text1[2]='t' == text2[4]='t' -> 1 + dp[3][5] = 1 + 0 = 1
        #   dp[1][2]: text1[1]='a' == text2[2]='a' -> 1 + dp[2][3]
        #                                          = 1 + 1 = 2
        #   dp[0][0]: text1[0]='c' == text2[0]='c' -> 1 + dp[1][1] = 1 + 2 = 3
        #
        # Answer = dp[0][0] = 3  ("cat")

        dp = [[ 0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                # go from diagonal +1
                if text1[i] == text2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                # go from max right or down
                else:
                    dp[i][j]=max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]