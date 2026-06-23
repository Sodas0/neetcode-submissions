class Solution:


    def encode(self, strs: List[str]) -> str:
        # iterate through the list (each iteration will be a string)
        res = ""
        for string in strs:
            # find length of each string
            temp_str = str(len(string))
            # append a delimiter to temp before concating with res
            temp_str = temp_str + "@" + string
            res = res + temp_str    
        return res
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0 # initially start of digits that signify len.

        while i < len(s): # find the delimiter.
            # use second pointer to keep track of the value of length in the string. # 
            j = i
            while s[j] != "@":
                j += 1 ## IMPORTANT: j is the index of the delimiter.

            length = int(s[i:j]) # s[i:j] at this point should be a string of an int. remember that slicing [i:j] does NOT include j.
            
            decoded.append(s[j+1:j+1+length]) # s[j+1] is start of word. j + 1 is start of the word, + length is end of the word.
            # then set i to the end of the word to begin the loop again.
            i = j +1+ length 
        return decoded
# [5@Hello2@Hi]
   