# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt=defaultdict(int)
        pair_cnt=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                pair_cnt[product]+=product_cnt[product]
                product_cnt[product]+=1
        res=0
        for cnt in pair_cnt.values():
            res+=8*cnt
        return res


        