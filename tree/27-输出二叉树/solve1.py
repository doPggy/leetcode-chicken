# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/print-binary-tree/
class Solution:
    # 我一直去找规律去了，算一行该有几个 ""
    # 卡在这里自然就不会去考虑递归该怎么写
    def height(self, root):
        if not root:
            return 0
        left_h  = self.height(root.left)
        right_h = self.height(root.right)
        return max(left_h, right_h) + 1
    def gen_array(self, h):
        col = 2 ** h - 1 # 一棵完全二叉树会有多少节点。
        return [ [ "" for j in range(col) ] for i in range(h) ]

    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        h          = self.height(root)
        array      = self.gen_array(h)
        def fill(root, h, left, right):
            if not root:
                return
            mid = (left + right) // 2
            array[h][mid] += str(root.val)
            fill(root.left, h + 1, left, mid - 1)
            fill(root.right, h + 1, mid + 1, right)
        fill(root, 0, 0, (2 ** h - 1) - 1)
        return array