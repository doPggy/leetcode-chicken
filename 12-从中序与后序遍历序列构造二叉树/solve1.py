# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归版本
    # 从后序知道根节点，然后根节点左边的值一定是在左子树中，右边的值一定在右子树
    # 然后对于这些左子树右子树，依旧需要做这样的操作
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def helper(in_left, in_right):
            if in_left > in_right:
                return
            # 直接 pop 也没啥
            #* 找到当前子树的根节点
            root_val   = postorder.pop()
            root_index = val_index[root_val]
            #! 先递归构造右子树
            right_root  = helper(root_index + 1, in_right)
            left_root   = helper(in_left, root_index - 1)
            # 构造一棵树
            root       = TreeNode(root_val)
            root.left  = left_root
            root.right = right_root
            return root
            
        val_index = { val:index for index, val in enumerate(inorder) }
        return helper(0, len(inorder) - 1)