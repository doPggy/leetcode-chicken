# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
class Solution:
    # 自顶向下，要让当前节点自己节点的相关 数据例如深度
    # 自定向下可以想到, 先序遍历，层序遍历

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [ root, ]
        len_q = 1
        level = 0
        while len_q > 0:
            while len_q > 0:
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                len_q -= 1
            len_q = len(queue)
            level += 1
        return level
