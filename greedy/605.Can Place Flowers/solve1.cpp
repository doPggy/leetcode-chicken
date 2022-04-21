// 另外一个题解

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int s = flowerbed.size();
        //! 这两个还是要注意
        flowerbed.push_back(0);
        flowerbed.insert(flowerbed.begin(), 0);
        //! 关键在于跳格子
        for(int i = 1; i <= s && n > 0;)
        {
            // 如果不能种，相邻也不能 直接跳
            if(flowerbed[i] == 1)
            {
                i += 2;
            }
            // 当前格为 0
            //! 前一格必定为 0 因为不能相邻种花
            else if(flowerbed[i + 1] == 0 || i == s)
            {
                // flowerbed[i] =1;
                --n;
                i += 2;
            }
            // 当前为 0 右边为 1 起码三格
            else
            {
                i += 3;
            }
        }

        // !
        return (n <= 0);
    }
};