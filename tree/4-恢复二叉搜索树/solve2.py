# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/recover-binary-search-tree/
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack   = []
        first   = None
        second  = None
        pre     = None
        # 直接不要另外的空间存中序遍历了
        # 只要记录上一个节点，当前节点比当前要小，就说明找到了
        # [1, 7, 5, 6 ,3, 8]
        while len(stack) > 0 or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not pre:
                pre  = root
                root = root.right
                continue
            elif pre.val > root.val:
                # 第二个位置是要下一个节点
                # 找到 6 的下一个 3
                second = root
                if not first:
                    # 第一个位置是要前一个节点
                    # 找到 7
                    first = pre
            pre  = root
            root = root.right
        
        first.val, second.val = second.val, first.val
        
        