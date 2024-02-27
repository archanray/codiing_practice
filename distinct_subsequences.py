# Given two strings s and t, return the number of distinct subsequences of s which equals t.
class Solution:
    def numDistinct(self, s, t):
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
# Time complexity: O(mn), where m is the length of s and n is the length of t.
# Space complexity: O(mn).
# Test case:
# "rabbbit", "rabbit"
# "babgbag", "bag"
# "a", "a"
# "a", "b"
# "a", ""
# "a", "a"
input = "rabbbit"
target = "rabbit"
print(Solution().numDistinct(input, target))