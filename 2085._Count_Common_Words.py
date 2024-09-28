# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

# Solution

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count_common=0
        if len(words1)>=len(words2):
            for value in words2:
                if words1.count(value)==1 and words2.count(value)==1:
                    count_common+=1
        else:
            for value in words1:
                if words1.count(value)==1 and words2.count(value)==1:
                    count_common+=1
        return count_common

