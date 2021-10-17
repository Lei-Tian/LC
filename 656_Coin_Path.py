class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n, memo = len(coins), {}
        memo[n - 1] = [[n], 0]
        path, cost = self.helper(0, coins, maxJump, memo)
        if cost >= sys.maxsize:
            return []
        return path

    def helper(self, index, coins, maxJump, memo):
        if index in memo:
            return memo[index]
        path, cost = [], sys.maxsize
        for jump in range(1, maxJump + 1):
            if index + jump < len(coins) and coins[index + jump] != -1:
                next_path, next_cost = self.helper(index + jump, coins, maxJump, memo)
                if cost > next_cost or path > next_path:
                    cost = next_cost
                    path = next_path

        memo[index] = [[index + 1] + path, cost + coins[index]]
        return memo[index]
