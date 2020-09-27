# https://leetcode-cn.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack   = [ root, ]
        cur_sum = [ sum, ]
        while len(stack) > 0:
            root = stack.pop()
            sum  = cur_sum.pop()
            if not root.right and not root.left:
                if root.val == sum:
                    return True
            if root.right:
                stack.append(root.right)
                cur_sum.append(sum - root.val)
            if root.left:
                stack.append(root.left)
                cur_sum.append(sum - root.val)
        return False