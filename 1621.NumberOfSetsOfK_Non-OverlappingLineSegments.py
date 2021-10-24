#!/usr/bin/env python
# coding=utf-8
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [[[0, 0] for j in range(k + 1)] for i in range(n)]
        MOD = 10**9 + 7
        for i in range(n):
            dp[i][0][0] = 1
            
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = sum(dp[i - 1][j])
                dp[i][j][1] = dp[i - 1][j][1]
                if j > 0:
                    dp[i][j][1] += sum(dp[i - 1][j - 1])
                dp[i][j][1] %= MOD
        
        return sum(dp[n - 1][k]) % MOD
