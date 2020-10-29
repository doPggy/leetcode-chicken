# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/merge-two-binary-trees/
class Solution:
    # 整体的大概我是了解的，但是细节或者说关键我没跟上
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 这个处理方式我一直没学会
        if not t1:
            return t2
        if not t2:
            return t1
        root         = TreeNode(t1.val + t2.val)
        queue_t1     = [ t1 ]
        queue_t2     = [ t2 ]
        queue_node   = [ root ]
        queue_t1_len = 1
        queue_t2_len = 1
        while len(queue_t1) > 0 and len(queue_t2) > 0:
            t1   = queue_t1.pop(0)
            t2   = queue_t2.pop(0)
            node = queue_node.pop(0)
            left1 = t1.left
            left2 = t2.left
            if left1 or left2:
                if left1 and left2:
                    node.left = TreeNode(left1.val + left2.val)
                    #? 这个不太懂
                    queue_node.append(node.left)
                    queue_t1.append(left1)
                    queue_t2.append(left2)
                elif left1:
                    # node.left = TreeNode(left1.val)
                    node.left = left1
                elif left2:
                    node.left = left2
            right1 = t1 and t1.right or None
            right2 = t2 and t2.right or None
            if right1 or right2:
                if right1 and right2:
                    node.right = TreeNode(right1.val + right2.val)
                    #? 这个不太懂
                    queue_node.append(node.right)
                    queue_t1.append(right1)
                    queue_t2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2
        return root