"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from collections import deque


# 记忆化搜索
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        d = set(wordDict)
        return self.helper(s, d, {})

    def helper(self, s, d, memo):
        # 在记忆中，直接返回
        if s in memo:
            return memo[s]
        # 整个字符串是一个单词，记住并返回
        if s in d:
            memo[s] = True
            return True
        # 尝试每个分割点
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            # 找s的解
            if right in d and self.helper(left, d, memo):
                memo[s] = True
                return True
        # 没找到s的解，记住并返回
        memo[s] = False
        return False


# 动态规划
class Solution1:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


# BFS，使用visited数组来标记已经算过的位置
class Solution2:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        visited = [False] * n
        q = deque([0])
        while q:
            start = q.popleft()
            if not visited[start]:
                for i in range(start + 1, n + 1):
                    if s[start:i] in wordDict:
                        q.append(i)
                        if i == n:
                            return True
                visited[start] = True
        return False


if __name__ == '__main__':
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
