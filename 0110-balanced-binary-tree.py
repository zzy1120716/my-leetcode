"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never
differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return True, 0
        isBalancedLeft, leftHeight = self.helper(root.left)
        if not isBalancedLeft:
            return False, 0
        isBalancedRight, rightHeight = self.helper(root.right)
        if not isBalancedRight:
            return False, 0
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1


# O(nlogn)
class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return abs(left_height - right_height) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


# O(n)
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        balanced, _ = self.height(root)
        return balanced

    def height(self, root):
        if not root:
            return True, 0
        balanced, left_height = self.height(root.left)
        if not balanced:
            return False, -1
        balanced, right_height = self.height(root.right)
        if not balanced:
            return False, -1
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
