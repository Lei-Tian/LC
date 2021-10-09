#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        # dp[i][j]: the min cost of paint houses[0:i] with house[i-1] paint with color[j]
        dp = [[0 for j in range(k)] for i in range(2)]
        
        for j in range(k):
            dp[0][j] = costs[0][j]
        
        now, old = 0, 1
        for i in range(1, n):
            firstIndex, secondIndex = self.updateIndex(None, None, dp[now])
            now, old = old, now
            for j in range(k):
                if j == firstIndex:
                    dp[now][j] = dp[old][secondIndex] + costs[i][j]
                else:
                    dp[now][j] = dp[old][firstIndex] + costs[i][j]
        return min(dp[now])
    
    def updateIndex(self, firstIndex, secondIndex, cost):
        for index in range(len(cost)):
            if firstIndex == None or cost[index] < cost[firstIndex]:
                secondIndex = firstIndex
                firstIndex = index
            elif secondIndex == None or cost[index] < cost[secondIndex]:
                secondIndex = index
        return firstIndex, secondIndex
