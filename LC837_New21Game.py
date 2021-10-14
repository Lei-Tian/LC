#!/usr/bin/env python
# coding=utf-8
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp[i]: the probability that Alice has n or fewer points when starting with i points
        # dp[i] = dp[i + 1] * (抽一次牌抽中1的概率) + dp[i + 2] * (抽一次牌抽中2的概率) + ... + dp[i + maxPts]) * (抽一次牌抽中maxPts的概率)
        # since (抽一次牌抽中j的概率) = 1 / maxPts
        # dp[i] = (dp[i + 1] + dp[i + 2] + ... + dp[i + maxPts]) / maxPts
        dp = [0 for i in range(k + maxPts)]
        for i in range(k, min(k + maxPts, n + 1)):
            dp[i] = 1
        
        # sliding window
        window_sum = min(n - k + 1, maxPts)
        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / float(maxPts)
            window_sum += dp[i] - dp[i + maxPts]
        
        return dp[0]
