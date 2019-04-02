"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        results = []
        if not root:
            return results

        stack = [root]

        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return results


class Solution1:
    def preorderTraversal(self, root: TreeNode):
        results = []
        if not root:
            return results
        rights = []

        node = root
        while node:
            results.append(node.val)
            if node.right:
                rights.append(node.right)
            node = node.left
            if not node and len(rights) != 0:
                node = rights.pop()

        return results


if __name__ == '__main__':
    import tools

    t1 = tools.Tree()
    t1.construct_tree([1, 2, 3, 4, 5, 6, 7])
    print(Solution().preorderTraversal(t1.root))
