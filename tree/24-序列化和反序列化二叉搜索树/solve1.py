# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        stack      = [ root ]
        serial_str = ""
        while len(stack) > 0:
            root = stack.pop()
            if not root:
                serial_str += "None,"
            else:
                serial_str += str(root.val) + ","
                stack.append(root.right)
                stack.append(root.left)
                root = root.left
        # print(serial_str[:-1])
        return serial_str[:-1]
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # def helper():
        serial_list = data.split(',')
        # print(serial_list)
        def helper():
            elem = serial_list.pop(0)
            if elem == 'None':
                return
            root        = TreeNode(int(elem))
            root.left   = helper()
            root.right  = helper()
            return root
        return helper()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans