# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue     = [ root ]
        len_queue = 1
        while len_queue > 0:
            i = 0
            while i < len_queue:
                if queue[i] is None:
                    val_1 = None
                else:
                    val_1 = queue[i].val
                if queue[len_queue - i - 1] is None:
                    val_2 = None
                else:
                    val_2 = queue[len_queue - i - 1].val
                if val_1 is None and val_2 is None:
                    i += 1
                    continue
                elif val_1 is None and val_2 is not None:
                    return False
                elif val_1 is not None and val_2 is None:
                    return False
                elif val_1 != val_2:
                    return False
                i += 1
            while len_queue > 0:
                root = queue.pop(0)
                if root:
                    queue.append(root.left)
                    queue.append(root.right)
                len_queue -= 1
            len_queue = len(queue)
        return True
                