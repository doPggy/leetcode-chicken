# https://leetcode-cn.com/problems/unique-binary-search-trees/
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 1
        c_i = 1
        for i in range(n):
            #计算 n 次，所以最后一次 c_i 就是 cn 得值
            c_i = c_i * 2 * (2 * i + 1) / (i + 2)
        return int(c_i)