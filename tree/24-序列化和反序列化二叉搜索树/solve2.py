# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/
class Codec:

    def int_2_str(self, x):
        # 4 个字节的数据分别放入数组
        byte_list = [ chr(x >> (i * 8) & 0xff) for i in range(4) ]
        byte_list.reverse()
        byte_str = ''.join(byte_list)
        return byte_str 

    def str_2_int(self, byte_s):
        r = 0
        # 一个字节一个字节读取
        for x in byte_s:
            r = r * 256 + ord(x)
        return r
    
    def pre_order(self, root):
        if not root:
            return []
        return [root.val] + self.pre_order(root.left) + self.pre_order(root.right)

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        order      = self.pre_order(root)
        byte_order = [ self.int_2_str(elem) for elem in order ]
        # print(byte_order)
        return ''.join(map(str, byte_order))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(left = float('-inf'), right = float('inf')):
            # 不在这个区间或者已经遍历完就返回
            if not pre_order or pre_order[-1] < left or pre_order[0] > right:
                return None
            val       = pre_order.pop(0)
            root      = TreeNode(val)
            root.left = helper(left, val)
            root.right = helper(val, right)
            return root
        n = len(data)
        # 最难搞部分就是这个，直接解码
        pre_order = [ self.str_2_int(data[i * 4 : (i + 1) * 4]) for i in range(n // 4) ]
        # return data
        return helper()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans