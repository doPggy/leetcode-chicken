# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/binary-tree-right-side-view/
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [ root ]
        order = []
        queue_len = len(queue)
        while queue_len > 0:
            while queue_len > 0:
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                queue_len -= 1
            order.append(root.val)
            queue_len = len(queue)

        return order
