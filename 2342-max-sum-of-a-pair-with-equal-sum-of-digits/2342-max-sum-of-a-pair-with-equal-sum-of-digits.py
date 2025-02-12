class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        DS=defaultdict(list)

        for num in nums:
            t, tnum=0,num
            while num:
                t+=num%10
                num //=10
            DS[t].append(tnum)

        res=-1
        for v in DS:
            if len(DS[v])>=2:
                res=max(res,sum(heapq.nlargest(2,DS[v]))) 
        return res
        