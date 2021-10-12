#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[2], dp[3] = 1, 2
        for i in range(4, n + 1):
            dp[i] = ((i - 1) * (dp[i - 2] + dp[i - 1])) % (10 ** 9 + 7)
        
        return dp[n] % (10 ** 9 + 7)
