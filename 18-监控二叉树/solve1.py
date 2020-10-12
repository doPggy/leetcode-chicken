# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/binary-tree-cameras/

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return 0, False
            if not root.left and not root.right:
                return 0, False
            left_min_camera_num, left_has_check   = helper(root.left)
            right_min_camera_num, right_has_check = helper(root.right)
            print(left_min_camera_num, left_has_check)
            print(right_min_camera_num, right_has_check)

            # 左右都有摄像机
            if left_has_check and right_has_check:
                return left_min_camera_num + right_min_camera_num, False
            # 左右没有摄像机
            elif not left_has_check and not right_has_check: 
                return left_min_camera_num + right_min_camera_num + 1, True
            # 一边有，一边没有
            elif left_has_check and not right_has_check:
                if root.right:
                    return left_min_camera_num + right_min_camera_num + 1, True 
                else:
                    return left_min_camera_num + right_min_camera_num, False 
            elif not left_has_check and right_has_check:
                if root.left:
                    return left_min_camera_num + right_min_camera_num + 1, True 
                else:
                    return left_min_camera_num + right_min_camera_num, False 
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        num, _ = helper(root)
        return num