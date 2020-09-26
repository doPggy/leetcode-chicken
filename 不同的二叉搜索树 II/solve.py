# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # 如果遍历到一个为 i 的节点
        # [1, i - 1] i [i + 1, n] 三个部分
        # 只要求出左右子树的所有组合，然后每个组合与 i 组成一个完整树，这个就是一个结果
        # 而左边要求出所有的组合，其实也是一样的操作。所以子问题都是一样且重复的，但只是规模变化了
        def gen(start, end):
            if start > end:
                return [ None, ]
            
            all_trees = []
            for i in range(start, end + 1):
                lefts  = gen(start, i - 1)
                rights = gen(i + 1, end)

                for l in lefts:
                    for r in rights:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        all_trees.append(cur)
            return all_trees
        return gen(1, n) if n != 0 else []