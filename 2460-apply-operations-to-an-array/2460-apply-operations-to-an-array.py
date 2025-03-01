class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(l-1):
            if nums[i]!=nums[i+1]:
                continue
            else:
                nums[i]*=2
                nums[i+1]=0
        non_zeroes, zeroes=[],[]
        for i in nums:
            if i==0:
                zeroes.append(i)
            else:
                non_zeroes.append(i)
        return non_zeroes+zeroes