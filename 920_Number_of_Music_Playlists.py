class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0 for j in range(goal + 1)] for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, goal + 1):
                dp[i][j] += dp[i - 1][j - 1] * (n - i + 1) # play i-th song
                if i > k:
                    dp[i][j] += dp[i][j - 1] * (i - k) # not play i-th song


        return dp[n][goal] % (10 ** 9 + 7)
    
