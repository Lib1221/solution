class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int l=0;
        for(int i=1;i<nums.size();i++){
            if(nums[l]!=0){
                l++;
            }
            else if(nums[l]!=nums[i]){
                swap(nums[l],nums[i]);
                l++;
            }
        }
        return;
    }
};