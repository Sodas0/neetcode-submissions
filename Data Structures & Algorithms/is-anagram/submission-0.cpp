#include <string>
#include <iostream>
#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        // before impl: use a hashmap to keep track of number of letters.
        // add to the hashmap for each new letter seen when iterating through first string.
        // when iterating through the second string, decrement the values depending on the letter.
        // if at the end the map's values are 0, they are anagrams. 
        std::unordered_map<char, int> num_letters;

        // eg: 
        // s = 'jar' ; t = 'jam'
        // pass through s:
            // num_letters = {j:1, a:1, r:1}
        // pass through t:
            // num_letters = {j:0, a:1, }
        //trivial check:
        if(s.size()!=t.size()){
            return false;
        }
        //pass through string s
        for(int i=0; i<s.size(); i++){
            if(num_letters.count(s[i]) > 0){
                num_letters[s[i]]++;
            }
            else{
                num_letters[s[i]]=1;
            }
        }
        //pass through string t. this is where we decrement.
        for(int i=0; i<s.size(); i++){
            if(num_letters.find(t[i]) != num_letters.end() && num_letters.count(t[i]) > 0){ //potential issue: num_letters[t[i]] dne.
                num_letters[t[i]]--;
            }
            else{ // something doesn't match, so not anagram
                return false;
            }
        }

        // check if map contains only 0s
        for (const auto& pair : num_letters) {
        if (pair.second != 0) {
            return false; // Found a different value
            }
        }

        return true;

    
    }
};
