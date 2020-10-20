# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/binary-tree-paths/
class Solution:
    def path():
        pass

    def binaryTreePaths(self, root: TreeNode) -> List[str]:            


        paths = [ str(root.val) + '->' ]
        def helper(root):
            if not root:
                return
            n = len(paths)
            for i in range(n):
                paths[i] += str(root.val) + "->"
            helper(root.left)
            helper(root.right)

        helper(root)
        print(paths)
            # if not root.left and not root.right:
            #     return [ "->" + str(root.val) ]
            # left_path   = None
            # right_path  = None 
            # if root.left:
            #     left_path  = helper(root.left)
            # if root.right:
            #     right_path = helper(root.right)

            # if left_path:            
            #     for path in left_path:
            #         pass

            # if lefts:
            #     return