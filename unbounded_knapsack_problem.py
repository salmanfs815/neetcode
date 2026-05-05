# https://neetcode.io/problems/unboundedKnapsack/question

# You are given a list of items, each with a weight and a profit, along with a
# backpack with a specified maximum capacity. Your goal is to calculate the
# maximum profit you can achieve without exceeding the backpack's capacity. You
# must select items such that the total weight of the items is less than or
# equal to the backpack's capacity. Assume you can select each item up to an
# unlimited number of times.

# Inputs:
# * profit - a list of n integers, where profit[i] represents the profit of the i-th item. (1 <= profit[i] <= 100)
# * weight - a list of n integers, where weight[i] represents the weight of the i-th item. (1 <= weight[i] <= 100)
# * capacity - an integer representing the maximum weight the backpack can hold. (1 <= capacity <= 100)

# Note: n is the number of items, where 1 <= n <= 100. You can assume that weight and profit are both the same length and only contain positive integers

# Example
# * Input:
#   * profit = [4, 4, 7, 1]
#   * weight = [5, 2, 3, 1]
#   * capacity = 8
# * Output: 18

# Solution 1: DFS with memoization
# Actual: 32ms runtime, 8.1MB memory usage
# class Solution:
#     def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
#         n = len(profit)
#         cache = [[-1] * (capacity + 1) for _ in range(n)]
#         def dfs(i, remCap):
#             if i == n:
#                 return 0
#             if cache[i][remCap] != -1:
#                 return cache[i][remCap]
#             skip = dfs(i + 1, remCap)
#             take = profit[i] + dfs(i, remCap - weight[i]) if remCap - weight[i] >= 0 else 0
#             maxProfit = max(skip, take)
#             cache[i][remCap] = maxProfit
#             return maxProfit
#         return dfs(0, capacity)

# Solution 2: DP
# Actual: 29ms runtime, 8.2MB memory usage
# class Solution:
#     def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
#         n = len(profit)
#         dp = [[0] * (capacity + 1) for _ in range(n)]
#         for i in range(n):
#             for c in range(1, capacity+1):
#                 skip = dp[i-1][c]
#                 take = profit[i] + dp[i][c - weight[i]] if c - weight[i] >= 0 else dp[i][c]
#                 dp[i][c] = max(skip, take)
#         return dp[-1][-1]

# Solution 3: DP - memory-optimized
# Actual: 29ms runtime, 7.9MB memory usage
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        prev = [0] * (capacity + 1)
        for i in range(n):
            curr = [0] * (capacity + 1)
            for c in range(1, capacity+1):
                skip = prev[c]
                take = profit[i] + curr[c - weight[i]] if c - weight[i] >= 0 else curr[c]
                curr[c] = max(skip, take)
            prev = curr
        return prev[-1]
