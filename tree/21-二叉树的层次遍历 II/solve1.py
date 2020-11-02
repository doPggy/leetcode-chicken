# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue       = [ root ]
        queue_len   = len(queue)
        order       = []
        while queue_len > 0:
            temp = []
            while queue_len > 0:
                root = queue.pop(0)
                temp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                queue_len -= 1
            order.insert(0, temp)
            queue_len = len(queue)
        return order
        # print(order[::-1])