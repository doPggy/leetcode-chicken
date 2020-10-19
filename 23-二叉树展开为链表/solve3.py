# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 差点前序写不出来
        if not root:
            return
        # 莫里斯遍历
        # 核心其实是对于当前节点，找到它的前驱节点
        while root:
            # print(root.val)
            # 叶子或者无左子树的节点
            if not root.left:
                # print(root.val)
                print(root.val)
                root = root.right # 因为 right 会指向右子树或者前驱
            else:
                tmp = root.left
                # 有可能是已经指向前驱
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                # 需要指向前驱 左子树最右节点
                if not tmp.right:
                    print(root.val)
                    tmp.right = root
                    root      = root.left
                else:
                    tmp.right = None
                    root      = root.right