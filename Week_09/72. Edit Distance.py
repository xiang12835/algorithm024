class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
        
        所以，

        当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；
        当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。

        第一行，是 word1 为空变成 word2 最少步数，就是插入操作

        第一列，是 word2 为空，需要的最少步数，就是删除操作

        T: O(mn)
        S: O(mn)
        """
        m, n = len(word1) , len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        # 第一行
        for j in range(n+1):
            dp[0][j] = j

        # 第一列
        for i in range(m+1):
            dp[i][0] = i
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 +  min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[m][n]