class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # track prefix sums for each element while iterating over nums. 
        # we can store prefix sums as values in a hashmap.
        # if prefix[j] - prefix[i] = 0, and j>i we know that the prefix sum from i+1 to j adds to 0.
        # we can extend this logic by saying:
        # if prefix[j] - prefix[i] = k, we can rearrange it to:
        #    prefix[j] = prefix[i]+k
        #    prefix[j]-k = prefix[i]
        # so then at position j, we can check if curr_sum - k = prefix[i], and if so, the subarray is from [i+1:j]
        curr_sum = 0
        freq_pref = {0:1} # initial state is we have seen pref sum of 0 1 time.
        num_subs = 0

        for num in nums:
            curr_sum+=num
            
            
            print(f"{curr_sum} - {k}: {curr_sum - k}")
            if curr_sum - k in freq_pref:
                num_subs += freq_pref[curr_sum-k]
            

            freq_pref[curr_sum] = freq_pref.get(curr_sum,0)+1
           
            
        
        return num_subs
