# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(in_left, in_right):
            if in_left > in_right:
                return
            # 当前根节点，且找到其中序遍历的位置
            root_val   = preorder.pop(0)
            root_index = val_index[root_val]
            # 其左便是左子树，其右便是右子树，但是这里是要先构造左子树
            left_root  = helper(in_left, root_index - 1)
            right_root = helper(root_index + 1, in_right)

            root       = TreeNode(root_val)
            root.left  = left_root
            root.right = right_root
            return root
            
        
        val_index = { val:index for index, val in enumerate(inorder) }
        return helper(0, len(inorder) - 1)