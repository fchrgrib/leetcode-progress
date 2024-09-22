class Solution {
public:
    int jump(vector<int>& nums) {
        int res = 0, i = 0, size = nums.size();
        if (size == 0 || size == 1) return 0;
        if (size == 2 && nums[0]!=0) return 1;

        while (i < size){
            if (i+nums[i]>= size-1) break;
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> temp;
            int jmp = nums[i];
            for(int j = i+1; j<=i+jmp; j++) temp.emplace(size - nums[j] - j, j);
            auto t = temp.top();
            i = t.second;
            res++;
        }

        return res+1;
    }
};