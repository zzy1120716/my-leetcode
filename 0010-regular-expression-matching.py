"""
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching
with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time.
Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


# 1. if p[j] == s[i]: dp[i][j] = dp[i - 1][j - 1]
# 2. if p[j] == '.':  dp[j][j] = dp[i - 1][j - 1]
# 3. if p[j] == '*':
# 3.1. if p[j - 1] != s[i]: dp[i][j] = dp[i][j - 2]
# (in this case, a* only counts as empty)
# 3.2. if p[j - 1] == s[i] or p[j - 1] == '.':
#    dp[i][j] = dp[i-1][j]   // in this case, a* counts as multiple a
# or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
# or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(n):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j + 1] or dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isMatch('xaabyc', 'xa*b.c'))
    print(Solution().isMatch('aab', 'c*a*b'))
