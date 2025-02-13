class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            if nums[0] >= k:
                return 0 
            else:
                return-1
        heapq.heapify(nums)
        count=0

        while nums[0]<k:
            a,b =heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums,a*2+b)
            count +=1

        return count
        