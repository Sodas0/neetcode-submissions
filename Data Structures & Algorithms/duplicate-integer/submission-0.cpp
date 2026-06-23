#include <iostream>
#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // naively: if it has a duplicate, you could use 2 for loops, but this bad.
        // let's use a hashmap, so O(n): for each element, add it to the hashmap after checking
        // its existence. if key already exists, hell naw.
        std::unordered_map<int, int> duplicates;
        std::size_t length = nums.size();

        for(int i=0; i<length; i++){
            if(duplicates.count(nums[i])>0){
                //key exists
                duplicates[nums[i]] += 1;
                return true;
            }
            else{
                duplicates[nums[i]] = 1;
            }
        }
        
        return false;

    }
};
