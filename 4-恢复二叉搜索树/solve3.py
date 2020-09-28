# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/recover-binary-search-tree/
class Solution:
    # 终于有点理解什么叫做树的很多问题是变相的遍历问题
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first   = None
        second  = None
        pre     = None
        # 莫里斯中序遍历需要安排一下
        # 在中序的遍历的时候，做一些逻辑而已，这大概就是框架思维
        while root:
            if not root.left:
                # 在这里判断的原因是，这里才是出序列的地方
                if not pre:
                    pre = root
                if pre.val > root.val:
                    second = root # 防止相邻情况
                    if not first:
                        first = pre
                pre  = root
                root = root.right
            else:
                tmp = root.left
                # 访问左子树的最右节点，中序遍历的前驱节点, 其实就是让前驱节点直接记录下一个节点
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                # 左子树遍历完毕, 开始右子树
                if tmp.right == root:
                    tmp.right = None
                    if not pre:
                        pre = root
                    # 在这里判断的原因是，这里才是出序列的地方
                    if pre.val > root.val:
                        second = root # 防止相邻情况
                        if not first:
                            first = pre
                    pre  = root
                    root = root.right
                # 记录
                else:
                    tmp.right = root
                    root      = root.left
        if first and second:
            first.val, second.val = second.val, first.val
