# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_word=0
        end=len(s)-1
        while end>=0:
            if s[end]==' ':
                if len_word !=0:
                    return len_word
            else:
                len_word+=1
            end-=1
        return len_word
        
        