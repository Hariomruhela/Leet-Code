class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        poscount=0
        negcount=0

        for num in nums:
            if (num>0):
                poscount+=1
            elif(num<0):
                negcount+=1

        return max(poscount, negcount)