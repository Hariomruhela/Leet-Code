# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        diff=float('inf')

        for i in range (len(nums)-2):
            l=i+1
            r= len(nums)-1
            
            while l<r:
                sum=nums[i]+nums[l]+nums[r]

                if (abs(sum-target)<diff):
                    diff=abs(sum-target)
                    newsum=sum
                    
                if sum==target:

                    return sum
                
                elif sum<target:
                    l+=1
                else:
                    r-=1
        return (newsum)
                