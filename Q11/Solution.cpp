class Solution {
public:
    int maxArea(vector<int>& height) {
        // Brute force will be find maximum of all combinations
        // Try to use sliding window method
        int i = 0, j = height.size() - 1;
        int maxArea = 0;
        while(i < j) {
            maxArea = max(min(height.at(i), height.at(j)) * (j - i), maxArea);
            if(height.at(i) > height.at(j)) {
                --j;
            }
            else{
                ++i;
            }
        }
        return maxArea;
    }
    
    int max(int a, int b) {
        return (a > b ? a : b);
    }
    
    int min(int a, int b) {
        return (a < b ? a : b);
    }
};
