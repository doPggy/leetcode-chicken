class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // example 1: [7,1,5,3,6,4]
        // 找升序，且找到这个序列中最大的那个
        int start = 0;
        int end   = 0;
        int len   = prices.size();
        int pre   = 0;
        int profit = 0;
        // for(int i = 0; ;)
        while(start < len && end < len)
        {
            if(prices[pre] <= prices[end])
            {
                pre = end++;
            }
            else
            {
                profit += prices[pre] - prices[start];
                start = pre = end;
                // pre    = end;
            }
        }

        //! pre 到顶了，说明还在升序
        // [1 2 3 4 5]
        if(pre == len - 1)
            profit += prices[pre] - prices[start];

        return profit;
    }
};