# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

class Codec:
    # 这他妈有重复值
    # 自己的想法是 前序 + 中序 构造
    # 但是题解用先序就能做了。
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 先序遍历编码
        def pre(root):
            if not root:
                return 'None,'
            s       = str(root.val) + ','
            left_s  = pre(root.left)
            right_s = pre(root.right)
            return s + left_s + right_s
        if not root:
            return ""
        return pre(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(order):
            val = order.pop(0)
            if val == 'None':
                return
            root       = TreeNode(int(val))
            root.left  = helper(order)
            root.right = helper(order)
            return root
        if data == "":
            return
        pre_order = data.split(',')
        return helper(pre_order)
