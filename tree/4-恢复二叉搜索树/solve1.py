# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode-cn.com/problems/recover-binary-search-tree/
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 利用中序遍历递增的特点, 如果两个节点被交换, 顶多两处非递增
        def in_order(root):
            stack = []
            order = []
            while len(stack) > 0 or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                order.append(root)
                root = root.right
            return order
        
        in_orders = in_order(root)
        # 找到两处非递增，交换空间
        # 还有一种情况 中序遍历结果为 [1 3 2 4]，只找到 first
        first     = None
        second    = None
        adjacent  = None
        for i in range(0, len(in_orders) - 1):
            if in_orders[i].val > in_orders[i + 1].val:
                if not first:
                    first    = in_orders[i]
                    adjacent = in_orders[i + 1]
                elif not second:
                    # 注意，第二个要找 i + 1 因为这个位置才是和 first 错误交换的节点
                    second = in_orders[i + 1]
                    break
        if first and second:
            first.val, second.val = second.val, first.val
        else:
            first.val, adjacent.val = adjacent.val, first.val
            
