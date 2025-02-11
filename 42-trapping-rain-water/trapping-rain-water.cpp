class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;

        int left = 0, right = n - 1;
        int left_max = height[left], right_max = height[right];
        int water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                left++;
                left_max = max(left_max, height[left]);
                water += max(0, left_max - height[left]);
            } else {
                right--;
                right_max = max(right_max, height[right]);
                water += max(0, right_max - height[right]);
            }
        }

        return water;
    }
};