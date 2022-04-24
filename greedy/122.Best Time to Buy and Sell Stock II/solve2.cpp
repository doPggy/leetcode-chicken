class Solution {
public:
    // 题解
    // https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode-s/
    int maxProfit(vector<int>& prices) {
        // example 1: [7,1,5,3,6,4]
        // 等价找 x 个不相交子集区间，使得利润最大
        // 那么就是相邻之间只要有利润可算，就加进来，这样就是和买入卖出的思路略微不匹配。
        int profit = 0;
        int len = prices.size();
        for(int i = 0; i < len - 1; i++)
        {
            profit += max(0, prices[i + 1] - prices[i]);
        }

        return profit;
       
    }
};