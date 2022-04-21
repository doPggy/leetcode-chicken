#include <vector>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int s = ratings.size();
        vector<int> candys(s, 1); // 初始化
        // 从左到右遍历一次, 右边评分高，就增加
        for(int i = 0; i < s - 1; i++)
        {
            if(ratings[i + 1] > ratings[i])
            {
                candys[i + 1] = candys[i] + 1;
            }
        }

        // 右边往左 
        for(int i = s - 1; i > 0; i--)
        {
            // 评分高，糖果分配要注意, 比左边评分高且糖果数更小才行
            if(ratings[i - 1] > ratings[i])
            {
                candys[i - 1] = max(candys[i - 1], candys[i] + 1);
            }
        }


        return accumulate(candys.begin(), candys.end(), 0);

    }
};