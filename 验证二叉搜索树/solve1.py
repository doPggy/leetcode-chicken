# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack    = []
        last_val = float("-inf")
        while len(stack) > 0 and root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop() # 中序
            if root.val <= last_val:
                return False
            last_val = root.val
            root     = root.right
        return True