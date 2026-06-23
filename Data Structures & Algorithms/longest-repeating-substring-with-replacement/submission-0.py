class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use a sliding window.
        # Maintain:
        # 1. A frequency map of characters in the window.
        #    A window is valid if (window_size - highest frequency in window) <= k.
        #    Otherwise, it must be repaired.
        # 2. max_so_far: the maximum length of any valid window seen.
        # 3. Two pointers (left, right) defining the window bounds.
        
        # Idea:
        # Start with left = 0 and expand the window by moving right.
        # If (window_size - highest frequency) > k, shrink the window from the left
        # until it becomes valid again.
        # After each expansion/repair, update max_so_far using (right - left + 1).

        left,right=0,0
        freq_map ={}
        max_so_far = 0

        for right in range(len(s)): # outer loop iterates through right pointer values.
            # add char to freq map
            if s[right] not in freq_map:
                freq_map[s[right]] = 1
            else: freq_map[s[right]] += 1

            window_length = right - left + 1 # 1-indexed
            max_freq = max(freq_map.values())

            while window_length - max_freq > k: # condition broken, repair window
                # first decrement left pointer's value from freq map, then increment the left pointer to move it up
                # this works because right pointer is guaranteed to have seen the value:
                freq_map[s[left]] -= 1
                left +=1
                # also need to decrease window length
                window_length -= 1
            
            # once here, the window is repaired, so update max so far.
            max_so_far = max(max_so_far, window_length)

        return max_so_far

            
