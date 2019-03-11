"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.dfs('', n, n, results)
        return results

    def dfs(self, path, left, right, results):
        if not left and not right:
            results.append(path)
            return

        if left > 0:
            self.dfs(path + '(', left - 1, right, results)
        if right > 0 and left < right:
            self.dfs(path + ')', left, right - 1, results)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
