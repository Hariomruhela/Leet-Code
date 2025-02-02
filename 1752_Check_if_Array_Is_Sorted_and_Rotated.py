# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        count=1
        for i in range(1, 2*n):
            if nums[(i-1)%n]<=nums[i%n]:
                count+=1
            else:
                count=1
            if count==n:
                return True
        
        return n==1
        