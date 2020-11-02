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
        #! 类莫里斯遍历
        # 遍历至叶子节点，记录返回其子树的上一层父节点
        #! 但是整道题是需要根据前序来改造, 找到前序遍历下，当前节点的前驱
        curr = root
        while curr:
            if curr.left:
                pre = tmp = curr.left
                # 有可能是已经指向前驱
                while tmp.right:
                    tmp = tmp.right
                # tmp 是 root.right 的前驱节点
                tmp.right  = curr.right
                curr.right = curr.left
                curr.left  = None
            curr = curr.right

