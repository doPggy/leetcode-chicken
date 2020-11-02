# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/binary-tree-paths/
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:            

        # 自顶向下，类先序
        # 为了 2->1 ... 这样的形式，其实也该想到先序
        def helper(root, path):
            if not root:
                return
            path += str(root.val)
            # 为叶子节点，那就结束了，加入答案中
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '->'
                helper(root.left, path)
                helper(root.right, path)

        paths = []
        helper(root, '')
        # print(paths)
        return paths