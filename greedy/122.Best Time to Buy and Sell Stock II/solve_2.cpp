class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 尽量找出利润大的不相交的区间，升序区间，但可以分割成一个一个
        int profit = 0;
        for(int i = 0; i < prices.size() - 1; i++)
        {
            profit += max(0, prices[i + 1] - prices[i]);
        }

        return profit;
    }
};