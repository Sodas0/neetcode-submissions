class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //naive solution: O(n^2):
        //  nested for loop; for each element in outer loop, compare the sum to other elements that are not the same element
        //    return true if sum = target, continue otherwise.
            
        for(int i=0; i<nums.size(); i++){
            for(int j=1; j<nums.size(); j++){
                if(i!=j && nums[i]+nums[j]==target){
                    return std::vector<int>{i,j};
                }
            }
        }
        return std::vector<int>{0,0};
    }
};


