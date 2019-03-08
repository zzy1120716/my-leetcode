"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 如果同时满足下面的条件，两个树互为镜像：
# 1. 它们的两个根结点具有相同的值。
# 2. 每个树的右子树都与另一个树的左子树镜像对称。

# 方法一：递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.check(root.left, root.right)

    def check(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            return left.val == right.val \
                   and self.check(left.left, right.right) \
                   and self.check(left.right, right.left)
        return False


# 方法二：非递归
# 当队列为空时，或者我们检测到树不对称
# （即从队列中取出两个不相等的连续结点）时，该算法结束。
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = []
        q.append(root)
        q.append(root)
        while len(q) != 0:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
