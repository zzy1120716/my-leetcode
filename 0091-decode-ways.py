"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


# DFS, TLE
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.dfs(0, s)

    def dfs(self, i, s):
        n = len(s)
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        res = self.dfs(i + 1, s)
        if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
            res += self.dfs(i + 2, s)
        return res


# 带记忆DFS
class Solution1:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        memo = [-1] * (n + 1)
        memo[n] = 1
        return self.dfs(0, s, memo)

    def dfs(self, i, s, memo):
        if memo[i] > -1:
            return memo[i]
        if s[i] == '0':
            memo[i] = 0
            return memo[i]
        res = self.dfs(i + 1, s, memo)
        if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
            res += self.dfs(i + 2, s, memo)
        memo[i] = res
        return res


# DP
class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    dp[i] += dp[i + 2]
        return 0 if n == 0 else dp[0]


if __name__ == '__main__':
    # print(Solution().numDecodings('12'))    # 2
    print(Solution2().numDecodings('2263124212'))   # 27
