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
        queue      = [ (root, 0, 2 ** h - 2) ]
        queue_len  = 1
        cur_row    = 0
        while queue_len > 0:
            while queue_len > 0:
                root, l, r = queue.pop(0)
                mid        = (l + r) // 2 
                array[cur_row][mid] += str(root.val)
                if root.left:
                    queue.append((root.left, l, mid - 1))
                if root.right:
                    queue.append((root.right, mid + 1, r))
                queue_len -= 1
            cur_row  += 1
            queue_len = len(queue)

        return array