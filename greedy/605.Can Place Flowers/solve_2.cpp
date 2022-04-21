class Solution {
public:
    // 关键利用花不相邻
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // flowerbed.in
        // flowerbed.insert(flowerbed.begin(), 0);
        int s = flowerbed.size();
        flowerbed.push_back(0);
        for(int i = 0; i < s; )
        {
            // 已经有花，寄了
            if(flowerbed[i] == 1)
            {
                i += 2;
            }
            // 判断右边有没有即可, 或者最后一位，
            else if(flowerbed[i + 1] == 0 || i == s - 1)
            {
                i += 2;
                --n;
            }
            else
            {
                i += 3;
            }
        }

        return n <= 0;
    }
};