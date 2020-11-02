# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/binary-tree-paths/
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:            
        if not root:
            return []

        # 广度优先遍历也可以做，这其实也应该作为框架的一种，但是我更侧重深度优先遍历了，导致忽略广度优先
        # 同广度遍历一样，对应的操作也可类似造一个队列
        node_queue = [ root ]
        path_queue = [ str(root.val) ]
        paths      = []
        while len(node_queue) > 0:
            root = node_queue.pop(0)
            path = path_queue.pop(0)

            if root.left:
                node_queue.append(root.left)
                path_queue.append(path + '->' + str(root.left.val))
            if root.right:
                node_queue.append(root.right)
                path_queue.append(path + '->' + str(root.right.val))

            if not root.left and not root.right:
                paths.append(path)
            
        return paths