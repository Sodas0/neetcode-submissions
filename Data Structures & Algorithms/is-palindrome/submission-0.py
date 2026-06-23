class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "case-insensitive and ignores all non-alphanumeric characters" --> remove punct -> remove spaces -> .lower()
        cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
        # pointers starting at i=0 and j=len(s)-1. check if s[i] != s[j]; return False if true

        i,j=0,len(cleaned_s)-1
        while i<j: 
            if cleaned_s[i]!=cleaned_s[j]:
                return False
            else:
                i+=1
                j-=1

        return True        