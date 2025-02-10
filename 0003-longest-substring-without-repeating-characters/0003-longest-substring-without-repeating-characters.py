class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        left=0
        ans=0
        for rigth in range(len(s)):
            while s[rigth] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[rigth])
            ans=max(ans,rigth-left+1)
        return ans


                    
        
