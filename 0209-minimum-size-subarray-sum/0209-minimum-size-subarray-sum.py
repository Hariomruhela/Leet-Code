class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        res=0
        curr=0
        n=len(nums)
        for i in range(n):
            curr+=nums[i]
            while curr>=target and start<n:
                if res==0:
                    res=i-start+1
                res=min(res,i-start+1)
                curr-=nums[start]
                start+=1
        return res
        