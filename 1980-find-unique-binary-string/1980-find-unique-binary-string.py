class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=""
        for i in range(len(nums)):
            cur=nums[i][i]
            res+="1" if cur=="0" else "0"
        

        return res