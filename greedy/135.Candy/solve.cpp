#include <algorithm>
#include <vector>

using namespace std;

// 思想就是和旁边那个人比，因为有左右，就搞两次
class Solution {
public:
    int candy(vector<int>& ratings) {
        int s = ratings.size();
        //! 极端情况
        if(s < 2) return s;
        vector<int> num(s, 1); // 初始化
        // 左到右
        for(int i = 0; i < s - 1; i++)
        {
            if(ratings[i + 1] > ratings[i])
                num[i + 1] =  num[i] + 1;
        }

        // 右到左
        //! 这里要注意，评分高且小于右边的糖果数才需要加
        for(int i = s - 1; i > 0; i--)
        {
            if(ratings[i - 1] > ratings[i])
                num[i - 1] = max(num[i - 1], num[i] + 1);
        }

        // int count = 0;
        // for(it : num)
        //     count += it;
        
        // return count;
        return accumulate(num.begin(), num.end(), 0); //!
    }
};