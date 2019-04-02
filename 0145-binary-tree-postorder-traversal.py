"""
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        results = []
        if not root:
            return results

        stack = [root]

        while stack:
            node = stack.pop()
            results = [node.val] + results
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return results


if __name__ == '__main__':
    import tools

    # t = tools.Tree()
    # t.construct_tree([1, None, 2, 3])
    # print(Solution().preorderTraversal(t.root))
    # print(Solution().postorderTraversal(t.root))

    t1 = tools.Tree()
    t1.construct_tree([1, 2, 3, 4, 5, 6, 7])
    # print(t1.pre_order_traversal())
    # print(t1.post_order_traversal())
    print(Solution().postorderTraversal(t1.root))
