#include <algorithm>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int s = flowerbed.size();
        // 头尾都插一个
        flowerbed.push_back(0);
        flowerbed.insert(flowerbed.begin(), 0);
        // 看右边就好
        for(int i = 1; i <= s;)
        {
            // 自己为 0，左右没有 1
            if(!flowerbed[i]
            && !flowerbed[i - 1]
            && !flowerbed[i + 1])
            {
                flowerbed[i] = 1;
                --n;
                i += 2; // 画图，可以知道不用判断相邻的了
            }
            else ++i;
        }
        if(n <= 0) return true;
        else return false;
    }
};