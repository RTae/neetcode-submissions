class Solution {
public:
    void sortColors(vector<int>& nums) {
        int range = 3;
        vector<int> count(range);
        for(int& num: nums) {
            count[num]++;
        }

        int index=0;
        for(int i = 0; i < range; i++) {
            while(count[i] > 0) {
                nums[index] = i;
                count[i]--;
                index++;
            }
        }
    }
};