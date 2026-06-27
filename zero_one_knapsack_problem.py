# read more: https://salmanfs.ca/posts/knapsack-problem/

# https://neetcode.io/problems/zeroOneKnapsack/question

# You are given a list of items, each with a weight and a profit, along with a
# backpack with a specified maximum capacity. Your goal is to calculate the
# maximum profit you can achieve without exceeding the backpack's capacity. You
# must select items such that the total weight of the items is less than or
# equal to the backpack's capacity. You can select at most one of each item.

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
# * Output: 12

# Solution 1: DFS
# Time: O(2^n), Space: O(n); where n is number of items
# Actual: [Time Limit Exceeded]
# class Solution:
#     def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
#         n = len(profit)
#         def dfs(i, remCap):
#             if i == n:
#                 return 0
#             skip = dfs(i + 1, remCap)
#             take = profit[i] + dfs(i + 1, remCap - weight[i]) if remCap - weight[i] >= 0 else 0
#             maxProfit = max(skip, take)
#             return maxProfit
#         return dfs(0, capacity)

# Solution 2: DFS with memoization
# Time: O(n * m), Space: O(n * m); where n is number of items and m is capacity
# Actual: 32ms runtime, 8.6MB memory usage
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
#             take = profit[i] + dfs(i + 1, remCap - weight[i]) if remCap - weight[i] >= 0 else 0
#             maxProfit = max(skip, take)
#             cache[i][remCap] = maxProfit
#             return maxProfit
#         return dfs(0, capacity)

# Solution 3: DP
# Time: O(n * m), Space: O(n * m); where n is number of items and m is capacity
# Actual: 29ms runtime, 8.2MB memory usage
# class Solution:
#     def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
#         n = len(profit)
#         dp = [[-1] * (capacity + 1) for _ in range(n)]
#         for i in range(n):
#             dp[i][0] = 0
#         for i in range(n):
#             for c in range(1, capacity + 1):
#                 skip = dp[i-1][c]
#                 take = profit[i] + dp[i-1][c - weight[i]] if c - weight[i] >= 0 else 0
#                 dp[i][c] = max(skip, take)
#         return dp[-1][-1]

# Solution 4: DP - memory-optimized
# Time: O(n * m), Space: O(m); where n is number of items and m is capacity
# Actual: 28ms runtime, 7.9MB memory usage
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        prev = [0] + ([-1] * (capacity))
        for i in range(n):
            curr = [0] + ([-1] * (capacity))
            for c in range(1, capacity + 1):
                skip = prev[c]
                take = profit[i] + prev[c - weight[i]] if c - weight[i] >= 0 else 0
                curr[c] = max(skip, take)
            prev = curr
        return prev[-1]
